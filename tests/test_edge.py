import os
from src.detection.edge import Edge

def test_demo_method():
    assert Edge()

def test_rename_images():
    os.chdir('images/people')
    files_list = os.listdir('.')
    i = 1
    for f in files_list:
        if f.endswith('.jpg'):
            os.rename(f, f'jpg_image{i:03d}.jpg')
            i += 1
