from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

from .Vocab import Vocab

class Captcha:
    '''
    size: width, height in pixel
    font: font family(string), size (unit pound) and font color (in "#rrggbb" format)
    bgcolor: in "#rrggbb" format
    '''

    def __init__(self, size, font, bgcolor, length = 4):
        #todo: add param check and transform here
        self.width, self.height = size
        self.font_family, self.font_size, self.font_color = font
        self.bgcolor = bgcolor
        self.len = length
        self.vocab = Vocab()
        self.font = ImageFont.truetype(self.font_family, self.font_size)
        
    def get_text(self):
        return self.vocab.rand_string(self.len)
    
    # by default, draw center align text
    def draw_text(self, str):
        dr = ImageDraw.Draw(self.im)
        font_width, font_height = self.font.getsize(str)
        # don't know why, but for center align, I should divide it by 2, other than 3
        randX = random.randint(1, self.width - font_width - 1)
        randY = random.randint(1, self.height - font_height - 1)
        
        #dr.text(((self.width - font_width) / 2, (self.height - font_height) / 2), str, fill = self.font_color, font = self.font)
        dr.text((randX, randY), str, fill = self.font_color, font = self.font)
    
    def draw_background(self):
        pass
    
    def filter(self):
        self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    
    # by default, add no noises
    def add_noise(self):
        pass
    
    def get_captcha(self):
        self.im = Image.new("RGB", (self.width, self.height), (self.bgcolor))
        self.draw_background()
        str = self.get_text()
        self.draw_text(str)
        self.add_noise()
        self.filter()
        return self.im, str

