from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random
def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255),random.randint(64, 255),random.randint(64, 255),)

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127), )

width = 60 * 4
height = 60
image = Image.new('RGB',(width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)

#im = Image.open('/home/alxl/Pictures/huxiao.JPG')
#w, h = im.size
#print('imagesize: %sx%s' % (w, h))
#
#im.thumbnail((w//2, h//2))
#im.save('thumbnail.jpg', 'jpeg')
