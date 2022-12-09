from pdf2image import convert_from_path
import os

path = 'docs/1.pdf'
images = convert_from_path(path)

for i in range(len(images)):
    target_path = 'page' + str(i + 1) + '.jpg'
    images[i].save(target_path, 'JPEG')
