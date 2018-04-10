from PIL import Image
import os
import glob

for filename in glob.glob('*.jpg'):
    image=Image.open(filename)
    print(str(image.filename) + ' format is => ' + str(image.mode))
    if image.mode == 'CMYK':
        print(str(image.filename) + ' format is now => ' + str(image.mode))
        image = image.convert('RGB').save(path_to_image)