import pytesseract as tess
import re
import os
import csv
from PIL import Image, ImageOps, ImageEnhance
from datetime import datetime
tess.pytesseract.tesseract_cmd = r'D:\\PythonProjects\\Tesseract-OCR\\tesseract.exe'

root = os.getcwd()
date = datetime.now()


# checks if 'files' folder if exists if not creates one
def files_workdir():
    try:
        if os.getcwd() == root:
            os.chdir('..')
        dirs = os.listdir()
        if 'files' in dirs:
            os.chdir('files')
        else:
            os.makedirs('files')
            os.chdir('files ')
    except:
        raise FileNotFoundError


# creates new folder everyday containing screenshots with format datetime m-d-y
def folder_date():
    file_path = os.getcwd()
    if root == file_path:
        files_workdir()
        file_path = os.getcwd()

    list_dirs = os.listdir()
    folder_name = date.strftime('%Y-%m-%d')
    
    if folder_name in list_dirs:
        os.chdir(folder_name)
    else:
        os.mkdir('{}\\{}'.format(file_path, folder_name))
        os.chdir(folder_name)


# appends to a txt file in type str for future purposes
def write_to_file(data):
    os.chdir(root)
    with open('data.txt', 'a') as file:
        file.write('{}\n'.format(str(data)))


# returns a dictionary of the text in the screenshots
def pytess():
    # start
    # os.chdir('..')
    # os.chdir('files\\date-of-folder')
    # end
    # use this if already have screenshots and import to rctweepy
    files = os.listdir()
    data = {}
    data['_id'] = date.strftime('%Y-%m-%d')
    for _file in files:
        img = Image.open(_file)
        greyimg = ImageOps.grayscale(img)
        invertimg = ImageOps.invert(greyimg)
        sharpimg = ImageEnhance.Sharpness(invertimg)
        factor = 1.25
        sharpened = sharpimg.enhance(factor)
        text = tess.image_to_string(sharpened, config="--psm 6")
        data['{}'.format(_file.strip('.png'))] = text.split()
    return data


def main():
    # os.chdir('..')
    # os.chdir('files\\12-08-2020')
    # dictt = pytess()
    # print(dictt)
    # print(type(dictt))
    # print(dictt['_id'])
    pass
if __name__ == '__main__':
    main()
    