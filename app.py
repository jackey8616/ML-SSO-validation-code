import keras
import requests
from sanic import Sanic
from sanic.response import json
from SSOModel import SSOModel

app = Sanic()

global model
model = SSOModel()
model.load()

@app.route('/validationCode', methods=['POST'])
async def validationCode(request):
    global model
    try:
        cookies = requests.utils.cookiejar_from_dict(request.cookies)
        for cookie in cookies:
            cookie.domain = 'webapp.yuntech.edu.tw'
        code = model.productionPredict(cookies=cookies)
        return json({ 'success': True, 'code': code })
    except Exception as e:
        return json({ 'fail': True, 'exception': e })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

