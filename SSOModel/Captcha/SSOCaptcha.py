from PIL import ImageDraw
import random

from . import Captcha

class SSOCaptcha(Captcha):

    def __init__(self,
                 size = (120, 40),
                 font = ("./SSOModel/font/arial.ttf", 25, "#FFFFFF"),
                 bgcolor = "#000000",
                 dot_rate = 0.075):
        Captcha.__init__(self, size, font, bgcolor)
        self.dot_rate = dot_rate
        
    def add_noise(self):
        dr = ImageDraw.Draw(self.im)
            
        # add pepper/salt noise.
        for w in range(self.width):
            for h in range(self.height):
                if random.randint(0, 100) / 100 <= self.dot_rate:
                    dr.point((w, h), fill = (255, 255, 255))
                    
    def draw_text(self, str):
        display_text = [" "] * (len(str) * 2 - 1)
        for i in range(len(str)):
            display_text[i * 2] = str[i]
        super().draw_text(str)

if __name__ == "__main__":
    captcha = SSOCaptcha()
    image, text = captcha.get_captcha()
    print(image, text)
