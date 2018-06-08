import requests, traceback
from io import BytesIO

from PIL import Image

urlCaptcha = 'https://webapp.yuntech.edu.tw/YunTechSSO/ImageValidationHandler.ashx'
    
def getImage(cookies=None):
    try:
        res = requests.get(urlCaptcha, cookies=cookies)
        image = Image.open(BytesIO(res.content))
        return image, 'IMGE'
    except Exception as e:
        traceback.print_exc()
        return None, None

if __name__ == "__main__":
    print(getImage())
