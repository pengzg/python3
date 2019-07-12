import tesserocr
from PIL import Image

image = Image.open('./images/code.jpg')
r = tesserocr.image_to_text(image)
print(r)

print(tesserocr.file_to_text('./images/code.jpg'))

print(tesserocr.file_to_text('./images/image.png'))

img = image.convert('L')
# img.show()
threshold = 110
table = []
for i in range(256):
    if i< threshold:
        table.append(0)
    else :
        table.append(1)
image = img.point(table, '1')
image.show()
res = tesserocr.image_to_text(image)
print(res)


