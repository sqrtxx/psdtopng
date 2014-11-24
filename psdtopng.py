from psd_tools import PSDImage
import sys
import os

def isfilepath(path):
    print(path)
    return os.path.isfile(os.path.abspath(os.path.expanduser(path)))

def ispsd(path):
    if path[-3:] == 'psd':
        return True
    return False

def pngpath(path):
    return path[:-3] + 'png'

file_paths = [file_path for file_path in sys.argv if isfilepath(file_path) and ispsd(file_path)]
for file_path in file_paths:
    psd = PSDImage.load(file_path)
    merged_image = psd.as_PIL()
    merged_image.save(pngpath(file_path))
