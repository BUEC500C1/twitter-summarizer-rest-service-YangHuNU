import os
from twitter_ import twitter_info
from PIL import Image, ImageDraw

# Create a background image and print twitter text on it

def generate_image(content, name):
	img = Image.new('RGB', (600,600), color='White')
	d = ImageDraw.Draw(img)
	d.text((10,10), content.encode('utf-8'), fill='Black')
	img.save('./images/'+ 'img_'+str(name)+'.png')


if __name__ == "__main__":
	generate_image("Penguins","test")