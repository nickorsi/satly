from PIL import Image
import requests

response = requests.get("https://saltly-bucket.s3.us-west-1.amazonaws.com/Nikon_COOLPIX_P1.jpg", stream=True)

with open("./static/Nikon_COOLPIX_P1.jpg", "wb") as outfile:
    outfile.write(response.content)

    breakpoint()
    # file = 'https://saltly-bucket.s3.us-west-1.amazonaws.com/Nikon_COOLPIX_P1.jpg'
img = Image.open("./static/Nikon_COOLPIX_P1.jpg")

img_bw = img.convert("L")
img.show()
img_bw.show()