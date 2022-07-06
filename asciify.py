import sys

import cv2
import numpy as np


# COLORS: https://github.com/onlyphantom/taskquant/blob/main/taskquant/utils/colors.py
SYMBOLS = [".", "\033[94m-\033[0m", "+", "*", "\033[92m#\033[0m", "o"]
THRESHOLDS = [0, 50, 100, 150, 200]

def print_symbols(array):
    """fill symbols in-place of numbers (index)
    """
    len_symbols = len(SYMBOLS)

    for row in array:
        for i in row:
            print(SYMBOLS[i % len_symbols], end="")
        print("")



def generate_ascii(img):
    """returns the numeric coded image
    """

    height, width = img.shape
    new_height = height // 6
    new_width = width // 3
    
    # resizing image to fit in console for printing
    resized_img = cv2.resize(img, (new_width, new_height))

    # [0, 0, 0, 0, 0]
    # [0, 0, 1, 0, 0]
    # [0, 0, 0, 2, 0]
    # [0, 4, 0, 0, 0]

    thresh_img = np.zeros(resized_img.shape)

    for i, threshold in enumerate(THRESHOLDS):
        thresh_img[resized_img > threshold] = i

    return thresh_img.astype(int)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(sys.argv)
        path = sys.argv[1]
    else:
        path = './assets/uk.png'

    img = cv2.imread(path, 0)
    ascii_art = generate_ascii(img)
    print_symbols(ascii_art)
