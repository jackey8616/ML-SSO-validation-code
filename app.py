import keras
import requests
from sanic import Sanic
from sanic.response import json
from SSOModel import SSOModel

app = Sanic()

global model
model = SSOModel()
model.load()

def validateCode(cookies):
    global model
    try:
        for cookie in cookies:
            cookie.domain = 'webapp.yuntech.edu.tw'
        code = model.productionPredict(cookies=cookies)
        return json({ 'success': True, 'code': code })
    except Exception as e:
        return json({ 'fail': True, 'exception': e })
    

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
    app.run(host='0.0.0.0', port=5000)

