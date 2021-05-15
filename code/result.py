import cv2
import numpy as np
import math
from matching import get_pixelvalue_black_sides
from music import play_music


def show_puzzle(total_pieces, smallest_length, smallest_width, result_array):
    # print_array(result_array)
    if total_pieces == 6:
        width_pieces = 3
        length_pieces = 2
    else:
        width_pieces = int(math.sqrt(total_pieces))
        length_pieces = int(math.sqrt(total_pieces))
    blank_image = np.zeros(shape=[smallest_length * length_pieces, smallest_width * width_pieces, 3], dtype=np.uint8)
    added_w = 0
    added_l = 0
    print("blank image:")
    print("length: ", blank_image.shape[0])
    print("width: ", blank_image.shape[1])
    print("------------------ ")
    # print("smallest image:")
    # print(smallest_length)
    # print(smallest_width)
    # print("------------------ ")
    cst_width_pieces = width_pieces

    for i in range(len(result_array)):
        black1_u, black1_l, black1_d, black1_r = get_pixelvalue_black_sides(result_array[i])
        image = result_array[i]
        length = image.shape[0]
        width = image.shape[1]
        # print("image:")
        # print(length)
        # print(width)
        # middle_l = round(blank_image.shape[0] / total_pieces) - black1_u
        # middle_w = round(blank_image.shape[1] / total_pieces) - black1_l
        new_l = smallest_length
        new_w = smallest_width
        # print("middle:")
        # print(middle_l)
        # print(middle_w)

        if i == 0:
            added_w = 0
            added_l = 0
        elif i < width_pieces:
            added_w += new_w
        if i == width_pieces:
            width_pieces += cst_width_pieces
            added_l += new_l
            added_w = 0

        print("width pieces:")
        print(width_pieces)
        print("piece:")
        print(i)
        # print("added:")
        # print(added_l)
        # print(added_w)
        # print("place on blank image:")
        # print("length", added_l, "-", smallest_length + added_l - black1_u + 1)
        # print("width: ", added_w, "-", smallest_width + added_w - black1_l + 1)
        print("place in array :")
        print("length", added_l, "-", length + added_l - black1_u + 1)
        print("width: ", added_w, "-", width + added_w - black1_l + 1)
        for j in range(width):
            for k in range(length):
                val = image[k][j][0] + image[k][j][1] + image[k][j][2]
                if val != 0:
                    blank_image[k + added_l - black1_u + 1][j + added_w - black1_l + 1][0] = image[k][j][0]
                    blank_image[k + added_l - black1_u + 1][j + added_w - black1_l + 1][1] = image[k][j][1]
                    blank_image[k + added_l - black1_u + 1][j + added_w - black1_l + 1][2] = image[k][j][2]
        print("------------------ ")
        cv2.imshow("new_image", blank_image)
        cv2.waitKey(500)
    return blank_image


def print_array(array):
    for i in range(len(array)):
        j = str(i)
        cv2.imshow("image" + j, array[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def add_music():
    print("music")
    winning_sound = ["f6", "8d#6", "8d6", "8c6", "p", "8g", "8a#", "p", "8d6", "c6", "p", "f6", "8d#6", "8d6", "8c6",
                     "p", "8d6",
                     "8a#", "p", "8d6", "c6", "p", "f6", "8d#6", "8d6", "8c6", "p", "8g", "8a#", "p", "8d6", "c6", "p",
                     "f6",
                     "8d#6",
                     "8d6", "8c6", "p", "8d6", "8a#", "p", "8d6", "c6"]

    play_music(winning_sound, 140, 5)
