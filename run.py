import requests, json

url = 'https://webapp.yuntech.edu.tw'
payload = { 'pStandardSubmit': False, 'pLoginName': '1234567', 'pLoginPassword': '1234567', 'pSecretString': ''}

session = requests.Session()
cookies = session.get(url + '/YunTechSSO/Account/Login').cookies

for i in range(30):

    codeRes = json.loads(requests.post('http://127.0.0.1:5000/validationCode',cookies=requests.utils.dict_from_cookiejar(cookies)).text)
    print(codeRes)

#import keras
#from SSOModel import SSOModel
#model = SSOModel()
#model.load()

#for i in range(4):
    #keras.backend.clear_session()
    #code = model.productionPredict(cookies=cookies)
    #codeRes = { 'success': True, 'code': code }

    if(codeRes['success'] == True):
        payload['pSecretString'] = codeRes['code']
        loginRes = session.post(url + '/YunTechSSO/Account/Login', data=payload)

        print(loginRes)
        print(loginRes.text)

        homeRes = session.get(url + '/YuntechSSO/Home/Index')

        print(homeRes)
        #print(homeRes.text)

