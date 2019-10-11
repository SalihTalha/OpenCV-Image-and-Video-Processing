from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from scipy import misc
import matplotlib.pyplot as plt

img = Image.open("./../data/scan1.jpg",'r')

draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./../res/FuturaExtended.ttf",25)
draw.text((x-r, y-h-35),"area: " + str(r*h*3.14/10),(255,255,0),font=font)
draw.ellipse((x-r, y-h, x+r, y+h), outline=(255,0,0,255))
draw = ImageDraw.Draw('image',img)

img.save("./../data/result1.png")