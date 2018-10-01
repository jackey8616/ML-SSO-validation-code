import keras, traceback, requests, click
from sanic import Sanic
from sanic.response import json
from SSOModel import SSOModel

app = Sanic()
model = None

@click.command()
@click.option('--model-folder', default='./SSOModel/model/', type=str)
@click.option('--debug', default=False, type=bool)
def run(model_folder, debug):
    global model, app
    model = SSOModel(model_folder=model_folder, debug=debug)
    model.load()
    app.run(host='0.0.0.0', port=5000)

def validateCode(cookies):
    global model
    try:
        for cookie in cookies:
            cookie.domain = 'webapp.yuntech.edu.tw'
        code = model.productionPredict(cookies=cookies)
        return json({ 'success': True, 'code': code })
    except Exception as e:
        return json({ 'fail': True, 'exception': traceback.format_exc() })
    

@app.route('/validationCode', methods=['POST'])
async def validationCode(request):
    try:
        print(request.cookies)
        cookies = requests.utils.cookiejar_from_dict(request.cookies)
        return validateCode(cookies)
    except Exception as e:
        return json({ 'fail': True, 'exception': e })

@app.route('/validationCode/cookieDict', methods=['POST'])
async def vcCookieDict(request):
    try:
        cookies = {}
        for (key, value) in request.json.items():
            cookies[key] = value['value']
        cookies = requests.utils.cookiejar_from_dict(cookies)
        return validateCode(cookies)
    except Exception as e:
        return json({ 'fail': True, 'exception': e })


if __name__ == '__main__':
    run()

