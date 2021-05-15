import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils
from extraction_original import *


def match_horizontal(method, image_left, image_right, border_left, border_right):
    print("--------new piece--------")
    if method != "shuffled":
        # Get rotated matches
        rotated_means = [1000, 1000, 1000, 1000]
        matches = [False, False, False, False]
        # print("border original: ", border_right)
        for i in range(4):
            angle = 90
            image_right, border_right = rotate_image(image_right, border_right, angle)
            # print("border rotated: ", border_right)
            if match_borders_horizontal(border_left, border_right):
                match_colors, rot_mean = match_colors_horizontal(image_left, image_right)
                if match_colors:
                    matches[i] = True
                    rotated_means[i] = rot_mean
            # cv2.imshow("left", image_left)
            # cv2.imshow("right", image_right)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        print("rotated all sides:")
        print(rotated_means)
        print(matches)

        match_bool = False
        match_smal = 1000
        match_rot = 0

        # Get best match from all matches
        smallest_rotated = min(i for i in rotated_means)
        for i in range(len(matches)):
            if matches[i] and smallest_rotated == rotated_means[i]:
                match_bool = True
                match_smal = smallest_rotated
                match_rot = i
        print("This is best match found in rotation:")
        print(match_bool)
        print(match_smal)
        return match_bool, match_smal, match_rot
    else:
        match = False
        mean = 1000
        if match_borders_horizontal(border_left, border_right):
            match_colors, mean = match_colors_horizontal(image_left, image_right)
            if match_colors:
                match = True
        # print(border_right)
        # print(border_left)
        # cv2.imshow("left", image_left)
        # cv2.imshow("right", image_right)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return match, mean, 0


def match_vertical(method, image_up, image_down, border_up, border_down):
    print("--------new piece--------")
    if method != "shuffled":
        # Get rotated matches
        rotated_means = [1000, 1000, 1000, 1000]
        matches = [False, False, False, False]
        # print("border original: ", border_down)
        for i in range(4):
            angle = 90
            image_down, border_down = rotate_image(image_down, border_down, angle)
            # print("border rotated: ", border_right)
            if match_borders_vertical(border_up, border_down):
                match_colors, rot_mean = match_colors_vertical(image_up, image_down)
                if match_colors:
                    matches[i] = True
                    rotated_means[i] = rot_mean
            # cv2.imshow("up", image_up)
            # cv2.imshow("down", image_down)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        print("rotated all sides:")
        print(rotated_means)
        print(matches)

        match_bool = False
        match_smal = 1000
        match_rot = 0
        # Get best match from all matches
        smallest_rotated = min(i for i in rotated_means)
        for i in range(len(matches)):
            if matches[i] and smallest_rotated == rotated_means[i]:
                match_bool = True
                match_smal = smallest_rotated
                match_rot = i
        print("This is best match found in rotation:")
        print(match_bool)
        print(match_smal)
        return match_bool, match_smal, match_rot
    else:
        match = False
        mean = 1000
        if match_borders_vertical(border_up, border_down):
            match_colors, mean = match_colors_vertical(image_up, image_down)
            if match_colors:
                match = True
        return match, mean, 0


def sort_images(all_array, array_borders):
    array_corner = []
    array_edge = []
    array_middle = []
    array_corner_types = []
    array_edge_types = []
    array_middle_types = []
    teller = 0
    for i in range(len(array_borders)):
        for j in range(len(array_borders[0])):
            if array_borders[i][j] == "S":
                teller += 1
        if teller == 0:
            array_middle.append(all_array[i])
            array_middle_types.append(array_borders[i])
        if teller == 1:
            array_edge.append(all_array[i])
            array_edge_types.append(array_borders[i])
        if teller == 2:
            array_corner.append(all_array[i])
            array_corner_types.append(array_borders[i])
        teller = 0
    return array_corner, array_edge, array_middle, array_corner_types, array_edge_types, array_middle_types


# compare 2 images
def match_borders(border_1, border_2):
    if border_1 == "M" and border_2 == "F":
        return True
    elif border_1 == "F" and border_2 == "M":
        return True
    else:
        return False


def match_borders_horizontal(border_types_left, border_types_right):
    is_match = False
    left = border_types_left[3]
    right = border_types_right[1]
    up1 = border_types_left[0]
    up2 = border_types_right[0]
    down1 = border_types_left[2]
    down2 = border_types_right[2]
    # print(left)
    # print(right)
    if match_borders(left, right):
        is_match = True
        if up1 == "S" and up2 != "S":
            is_match = False
        elif down1 == "S" and down2 != "S":
            is_match = False
    return is_match


def match_borders_vertical(border_types_up, border_types_down):
    is_match = False
    up = border_types_up[2]
    down = border_types_down[0]
    left1 = border_types_up[1]
    left2 = border_types_down[1]
    right1 = border_types_up[3]
    right2 = border_types_down[3]
    # print(up)
    # print(down)
    if match_borders(up, down):
        is_match = True
        if left1 == "S" and left2 != "S":
            is_match = False
        elif right1 == "S" and right2 != "S":
            is_match = False
    return is_match


def match_colors_horizontal(image_left, image_right):
    black1_u, black1_l, black1_d, black1_r = get_pixelvalue_black_sides(image_left)
    black2_u, black2_l, black2_d, black2_r = get_pixelvalue_black_sides(image_right)
    image_left = cv2.cvtColor(image_left, cv2.COLOR_RGB2HSV)
    image_right = cv2.cvtColor(image_right, cv2.COLOR_RGB2HSV)
    length1 = image_left.shape[0]
    length2 = image_right.shape[0]
    width1 = image_left.shape[1]
    width2 = image_right.shape[1]
    is_match = False
    match_hole = False
    # print(length1)
    # print(width1)
    # print(length2)
    # print(width2)
    # cv2.imshow("dsf", image_left)
    # cv2.imshow("im2 ", image_right)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    pixels = []
    teller = 0
    # print(length1 - black1_u - black1_d)
    total_l = min([length1 - black1_u - black1_d, length2 - black2_u - black2_d])

    for i in range(total_l):
        pixel1 = i + black1_u, width1 - 3 - black1_r
        pixel2 = i + black2_u, black2_l

        var1 = int(image_left[pixel1][0]) + int(image_left[pixel1][1]) + int(image_left[pixel1][2])
        var2 = int(image_right[pixel2][0]) + int(image_right[pixel2][1]) + int(image_right[pixel2][2])
        var = var1 - var2
        # print(var1)
        pixels.append(var)
        if var1 == 0:
            pixels.remove(var)
            pixel2 = i + black2_u, black2_l - 5
            try:
                var2 = int(image_right[pixel2][0]) + int(image_right[pixel2][1]) + int(image_right[pixel2][2])
                # print(var2)
            except:
                print("image is black")
            if var2 == 0:
                teller += 1
            if teller > 6:
                match_hole = False
            else:
                match_hole = True
        elif var2 == 0:
            pixels.remove(var)
            pixel1 = i + black1_u, width1 - 3 - black1_r + 5
            try:
                var1 = int(image_left[pixel1][0]) + int(image_left[pixel1][1]) + int(image_left[pixel1][2])
                # print(var1)
            except:
                print("image is black")
            if var1 == 0:
                teller += 1
            if teller > 6:
                match_hole = False
            else:
                match_hole = True
        # cv2.circle(image_left, pixel1, 2, (0, 255, 0))
        # print(pixel1)
        # print(image_left[pixel1])
        # cv2.circle(image_right, pixel2, 2, (0, 255, 0))
        # print(pixel2)
        # print(image_right[pixel2])
    mean = np.mean(np.absolute(pixels))
    # print(mean)
    # cv2.imshow("dsf", image_left)
    # cv2.imshow("im2 ", image_right)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    max = 500
    if mean < max:
        if match_hole:
            is_match = True

    print("color_match:")
    print(is_match)
    print(match_hole)
    return is_match, mean


def match_colors_vertical(image_up, image_down):
    black1_u, black1_l, black1_d, black1_r = get_pixelvalue_black_sides(image_up)
    black2_u, black2_l, black2_d, black2_r = get_pixelvalue_black_sides(image_down)
    # image_up = cv2.cvtColor(image_up, cv2.COLOR_RGB2HSV)
    # image_down = cv2.cvtColor(image_down, cv2.COLOR_RGB2HSV)
    length1 = image_up.shape[0]
    length2 = image_down.shape[0]
    width1 = image_up.shape[1]
    width2 = image_down.shape[1]
    is_match = False
    match_hole = False
    # print(length1)
    # print(width1)
    # print(black1_u)
    # print(black1_d)
    # print(length2)
    # print(width2)
    # print(length1 + black1_u - black1_d)

    # cv2.imshow("dsf", image_up)
    # cv2.imshow("im2 ", image_down)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    pixels = []
    teller = 0
    total_w = min([width1 - black1_l - black1_r, width2 - black2_l - black2_r])

    for i in range(total_w):
        pixel1 = length1 - black1_d - 2, i + black1_l  # length1 + black1_u - black1_d
        pixel2 = black2_u - 1, i + black2_l
        var1 = int(image_up[pixel1][0]) + int(image_up[pixel1][1]) + int(image_up[pixel1][2])
        var2 = int(image_down[pixel2][0]) + int(image_down[pixel2][1]) + int(image_down[pixel2][2])
        var = var1 - var2
        pixels.append(var)

        if var1 == 0:
            pixels.remove(var)
            pixel2 = black2_u - 1 - 2, i + black2_l
            try:
                var2 = int(image_down[pixel2][0]) + int(image_down[pixel2][1]) + int(image_down[pixel2][2])
                # print(var2)
            except:
                print("image is black")
            if var2 == 0:
                teller += 1
            if teller > 6:
                match_hole = False
            else:
                match_hole = True
        elif var2 == 0:
            pixels.remove(var)
            pixel1 = length1 - black1_d - 2 + 2, i + black1_l
            try:
                var1 = int(image_up[pixel1][0]) + int(image_up[pixel1][1]) + int(image_up[pixel1][2])
                # print(var1)
            except:
                print("image is black")
            if var1 == 0:
                teller += 1
            if teller > 6:
                match_hole = False
            else:
                match_hole = True
        # cv2.circle(image_up, (pixel1[1], pixel1[0]), 2, (0, 255, 0))
        # print(pixel1)
        # print(image_up[pixel1])
        # cv2.circle(image_down, (pixel2[1], pixel2[0]), 2, (0, 255, 0))
        # print(pixel2)
        # print(image_down[pixel2])
    # plot_axis = np.arange(len(pixels))
    # plt.plot(plot_axis, pixels)
    # plt.show()
    # plot_axis = np.arange(len(pixels_up))
    # plt.plot(plot_axis, pixels_up)
    # plot2_axis = np.arange(len(pixels_down))
    # plt.plot(plot_axis, pixels_down)
    # plt.show()
    mean = np.mean(np.absolute(pixels))
    # print(mean)
    max = 500
    if mean < max:
        if match_hole:
            is_match = True
    print("color_match:")
    print(is_match)
    print(match_hole)
    return is_match, mean


def get_pixelvalue_black_sides(image):
    length = image.shape[0]
    width = image.shape[1]
    total_array = []
    black_l = 0
    black_r = 0
    black_u = 0
    black_d = 0
    cst = 1
    value = 0
    median = 0
    while median < cst:
        for i in range(length):
            value += image[i][width - 1 - black_r][0]
            value += image[i][width - 1 - black_r][1]
            value += image[i][width - 1 - black_r][2]
            total_array.append(value)
            value = 0
        black_r += 1
        median = np.median(total_array)
        # print(total_array)
        total_array = []
    median = 0
    while median < cst:
        for i in range(length):
            value += image[i][black_l][0]
            value += image[i][black_l][1]
            value += image[i][black_l][2]
            total_array.append(value)
            value = 0
        black_l += 1
        median = np.median(total_array)
        total_array = []
    median = 0
    while median < cst:
        for i in range(1, width):
            value += image[black_u][i][0]
            value += image[black_u][i][1]
            value += image[black_u][i][2]
            total_array.append(value)
            value = 0
        black_u += 1
        median = np.median(total_array)
        total_array = []
    median = 0
    while median < cst:
        for i in range(width):
            value += image[length - 1 - black_d][i][0]
            value += image[length - 1 - black_d][i][1]
            value += image[length - 1 - black_d][i][2]
            total_array.append(value)
            value = 0
        black_d += 1
        median = np.median(total_array)
        total_array = []
    # print(black_u)
    # print(black_l)
    # print(black_d)
    # print(black_r)
    # print("------------")
    return black_u, black_l, black_d, black_r


def rotate_image(image, borders, angle):
    # print("rotate")
    # print(borders)
    rotated = imutils.rotate_bound(image, angle)
    if angle != 0:
        borders = borders[1:] + [borders[0]]

    # print(borders)
    # cv2.imshow("Rotated (Correct)", rotated)
    # cv2.waitKey(0)
    return rotated, borders
