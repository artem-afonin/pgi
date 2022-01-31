from os import path

import numpy as np
from PIL import Image


def main():
    script_path = path.abspath(__file__)
    script_dir = path.dirname(script_path)
    resources_dir = path.join(script_dir, '..', 'resources')
    img_path = path.abspath(path.join(resources_dir, 'cat.bmp'))

    img = Image.open(img_path)
    img_matrix = np.array(img.convert('RGB'))

    print(f'Format: {img.format}')
    print(f'Size: {img.size}')
    print(f'Mode: {img.mode}')

    for row in range(img.height):
        for col in range(img.width):
            pixel = img_matrix[row, col]
            mean = int(sum([pixel[0], pixel[1], pixel[2]]) / 3)
            img_matrix[row, col] = mean, mean, mean

    new_img = Image.fromarray(img_matrix, 'RGB')
    # new_img.save(path.join(resources_dir, 'cat_gray.bmp'), 'bmp')
    new_img.show()


if __name__ == '__main__':
    main()
