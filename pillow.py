from PIL import Image

file = './static/matt.jpg'
img = Image.open(file)

img_bw = img.convert("L")
img.show()
img_bw.show()
