import requests, traceback, base64, re
from io import BytesIO

from PIL import Image

urlCaptcha = 'https://webapp.yuntech.edu.tw/YunTechSSO/ImageValidationHandler.ashx'
    
def getImage(cookies):
    try:
        res = requests.get(urlCaptcha, cookies=cookies)
        image = Image.open(BytesIO(res.content))
        return image, 'IMGE'
    except Exception as e:
        traceback.print_exc()
        return None, None

def getImageByCookies(cookies):
    return getImage(cookies=cookies)

def getImageByBase64(base64Str):
    try:
        base64_data = re.sub('^data:image/.+;base64,', '', base64Str)
        byte_data = base64.b64decode(base64_data)
        image = Image.open(BytesIO(byte_data)).convert('RGB')
        return image, 'IMGE'
    except Exception as e:
        traceback.print_exc()
        return None, None


if __name__ == "__main__":
    print(getImage())
