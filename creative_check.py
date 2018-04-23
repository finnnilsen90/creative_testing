from PIL import Image
import os
import glob

for filename in glob.glob('*.jpg'):

    image=Image.open(filename)
    path = os.path.abspath(filename)

    print(str(image.filename) + ' CURRENT format is => ' + str(image.mode))
    if image.mode == 'CMYK': 
        image.convert('RGB').save(path)
        print(str(image.filename) + ' format is now => ' + str(image.mode))
    else:
        print(str(image.filename) + ' is good. format is => ' + str(image.mode))