from os import path
from random import randint

import numpy as np
from PIL import Image


def main():
    script_path = path.abspath(__file__)
    script_dir = path.dirname(script_path)
    resources_dir = path.join(script_dir, '..', 'resources')
    img_path = path.abspath(path.join(resources_dir, 'cat.bmp'))

    img = Image.open(img_path)
    img_matrix = np.array(img.convert('RGB'))

    for row in range(img.height):
        for col in range(img.width):
            if row < 15 or col < 15 or row > img.height - 15 or col > img.width - 15:
                img_matrix[row][col] = randint(0, 255), randint(0, 255), randint(0, 255)

    new_img = Image.fromarray(img_matrix, 'RGB')
    # new_img.save(path.join(resources_dir, 'cat_with_frame.bmp'), 'bmp')
    new_img.show()


if __name__ == '__main__':
    main()
