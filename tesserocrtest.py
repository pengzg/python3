import tesserocr
from PIL import Image

image = Image.open('./images/code.jpg')
r = tesserocr.image_to_text(image)
print(r)

print(tesserocr.file_to_text('./images/code.jpg'))