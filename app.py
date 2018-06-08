from gevent import monkey
monkey.patch_all()
from gevent.pywsgi import WSGIServer

import keras
import requests
from flask import Flask, request, jsonify
from SSOModel import SSOModel

app = Flask(__name__)

model = SSOModel()

@app.route('/validationCode', methods=['POST'])
def validationCode():
    try:
        cookies = requests.utils.cookiejar_from_dict(request.cookies)
        for cookie in cookies:
            cookie.domain = 'webapp.yuntech.edu.tw'
        keras.backend.clear_session()
        model.load()
        code = model.productionPredict(cookies=cookies)
        return jsonify({ 'success': True, 'code': code })
    except Exception as e:
        return jsonify({ 'fail': True, 'exception': e })

if __name__ == '__main__':
    server = WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()

