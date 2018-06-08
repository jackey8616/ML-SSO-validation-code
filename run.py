import requests

from SSOModel import SSOModel

model = SSOModel()
model.load()

url = 'https://webapp.yuntech.edu.tw'
payload = { 'pStandardSubmit': False, 'pLoginName': '1234567', 'pLoginPassword': '1234', 'pSecretString': ''}

session = requests.Session()
cookies = session.get(url + '/YunTechSSO/Account/Login').cookies
validationCode = model.productionPredict(cookies=cookies)

payload['pSecretString'] = validationCode
loginRes = session.post(url + '/YunTechSSO/Account/Login', data=payload)

print(loginRes)
print(loginRes.text)

homeRes = session.get(url + '/YuntechSSO/Home/Index')

print(homeRes)
#print(homeRes.text)

