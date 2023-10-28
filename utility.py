import sys
import os
import shutil
import time
from random import randint
from multiprocessing import Pool

import requests


def load_image(href: str) -> None:
    img = requests.get(href)
    with open(f'{randint(0,25)}.jpg', 'wb') as f:
        f.write(img.content)


def main() -> None:
    t1 = time.time()

    if os.path.isdir('images'):
        shutil.rmtree('images')
    os.mkdir('images')
    os.chdir('images')

    links = sys.argv[1:]

    with Pool(3) as p:
        p.map(load_image, links)

    print(time.time() - t1)
