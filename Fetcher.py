import requests
from io import BytesIO

from PIL import Image

urlCaptcha = 'https://webapp.yuntech.edu.tw/YunTechSSO/ImageValidationHandler.ashx'
    
def getImage(cookies=None):
    res = requests.get(urlCaptcha, cookies=cookies)
    image = Image.open(BytesIO(res.content))
    return image, 'IMGE'

if __name__ == "__main__":
    print(getImage())
