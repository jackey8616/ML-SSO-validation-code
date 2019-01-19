import keras, traceback, requests, click
from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from SSOModel import SSOModel
from SSOModel.Fetcher import getImageByCookies, getImageByBase64

app = Sanic()
model = None

@click.command()
@click.option('--model-folder', default='./SSOModel/model/', type=str)
@click.option('--debug', default=False, type=bool)
def run(model_folder, debug):
    global model, app
    model = SSOModel(model_folder=model_folder, debug=debug)
    model.load()
    CORS(app)
    app.run(host='0.0.0.0', port=5000)

def validateCodeByCookies(cookies):
    global model
    try:
        for cookie in cookies:
            cookie.domain = 'webapp.yuntech.edu.tw'
        img, text = getImageByCookies(cookies=cookies)
        code = model.productionPredict(img=img, text=text)
        return json({ 'success': True, 'code': code })
    except Exception as e:
        return json({ 'fail': True, 'exception': traceback.format_exc() })


def validateCodeByBase64(base64Str):
    global model
    try:
        img, text = getImageByBase64(base64Str=base64Str)
        code = model.productionPredict(img=img, text=text)
        return json({ 'success': True, 'code': code })
    except Exception as e:
        return json({ 'fail': True, 'exception': traceback.format_exc() })

@app.route('/validationCode', methods=['POST'])
async def validationCode(request):
    try:
        print(request.cookies)
        cookies = requests.utils.cookiejar_from_dict(request.cookies)
        return validateCodeByCookies(cookies)
    except Exception as e:
        return json({ 'fail': True, 'exception': e })

@app.route('/validationCode/cookieDict', methods=['POST'])
async def vcCookieDict(request):
    try:
        cookies = {}
        for (key, value) in request.json.items():
            cookies[key] = value['value']
        cookies = requests.utils.cookiejar_from_dict(cookies)
        return validateCodeByCookies(cookies)
    except Exception as e:
        return json({ 'fail': True, 'exception': e })

@app.route('/validationCode/base64', methods=['POST'])
async def vcBase64(request):
    try:
        base64Str = request.json['image']
        return validateCodeByBase64(base64Str=base64Str)
    except Exception as e:
        return json({ 'fail': True, 'exception': e })


if __name__ == '__main__':
    run()

