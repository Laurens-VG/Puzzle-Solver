import math
import cv2
from matching import *
global column


def solve_puzzle(total_pieces, method, array_c, array_e, array_m, array_c_types, array_e_types, array_m_types):
    print("Solving puzzle...")
    global column
    global method_used
    method_used = method
    total_pieces = int(total_pieces)
    if total_pieces != 6:
        row = int(math.sqrt(total_pieces))
        column = row
    else:
        row = 2
        column = 3
    result_array = []
    result_array_types = []
    for i in range(row):
        # FIRST ROW
        if i == 0:
            # start with left upper corner
            if method == "shuffled":
                index = 0
                for i in range(1, len(array_c_types)):
                    if array_c_types[i][0] == "S" and array_c_types[i][1] == "S":
                        index = i
                result_array.append(array_c[index])
                result_array_types.append(array_c_types[index])
                remove_array(array_c, array_c[index])
                array_c_types.remove(array_c_types[index])
            else:
                if array_c_types[0][0] != "S" or array_c_types[0][1] != "S":
                    array_c[0], array_c_types[0] = rotate_image(array_c[0], array_c_types[0], 90)
                # print(array_c_types[0][0], "+" ,array_c_types[0][1])
                if array_c_types[0][0] != "S" or array_c_types[0][1] != "S":
                    array_c[0], array_c_types[0] = rotate_image(array_c[0], array_c_types[0], 90)
                # print(array_c_types[0][0], "+" ,array_c_types[0][1])
                if array_c_types[0][0] != "S" or array_c_types[0][1] != "S":
                    array_c[0], array_c_types[0] = rotate_image(array_c[0], array_c_types[0], 90)
                index = 0
                try:
                    # print(array_c[index].shape[1])
                    # print(array_c[index].shape[0])
                    # print(array_c_types[index][0])
                    # print(array_c_types[index][1])
                    while total_pieces == 6 and array_c[index].shape[1] > array_c[index].shape[0] or array_c_types[index][0] != "S" and array_c_types[index][1] != "S":
                        index += 1
                        # cv2.imshow("im", array_c[index])
                        # cv2.waitKey()
                        # print(array_c_types[index])
                        if array_c_types[index][0] != "S" or array_c_types[index][1] != "S":
                            array_c[index], array_c_types[index] = rotate_image(array_c[index], array_c_types[index], 90)
                        # print(array_c_types[index][0], "+" ,array_c_types[index][1])
                        if array_c_types[index][0] != "S" or array_c_types[index][1] != "S":
                            array_c[index], array_c_types[index] = rotate_image(array_c[index], array_c_types[index], 90)
                        # print(array_c_types[index][0], "+" ,array_c_types[index][1])
                        if array_c_types[index][0] != "S" or array_c_types[index][1] != "S":
                            array_c[index], array_c_types[index] = rotate_image(array_c[index], array_c_types[index], 90)
                        # print(array_c_types[index][0], "+", array_c_types[index][1])
                        # cv2.imshow("im2", array_c[index])
                        # cv2.waitKey()
                        # print("index:", index)
                except:
                    print("index out of range")
                    index = 1
                # print(array_c_types[0])
                # cv2.imshow("corner", array_c[index])
                # cv2.waitKey()
                # cv2.destroyAllWindows()
                result_array.append(array_c[index])
                result_array_types.append(array_c_types[index])
                remove_array(array_c, array_c[index])
                array_c_types.remove(array_c_types[index])

            # start with an edge that matches with the other one
            for j in range(column - 2):
                # match piece with left piece
                result_array, result_array_types, array_e, array_e_types = get_match("horizontal", result_array, array_e, result_array_types, array_e_types)

            # end with corner
            result_array, result_array_types, array_c, array_c_types = get_match("horizontal", result_array, array_c, result_array_types, array_c_types)

        # LAST ROW
        elif i == row-1:
            # start with  corner
            result_array, result_array_types, array_c, array_c_types = get_match("vertical", result_array, array_c, result_array_types, array_c_types)

            # start with an edge that matches with the other one
            for j in range(column - 2):
                # match piece with left piece
                result_array, result_array_types, array_e, array_e_types = get_match("horizontal", result_array, array_e, result_array_types, array_e_types)

            # end with last corner
            result_array, result_array_types, array_c, array_c_types = get_match("horizontal", result_array, array_c, result_array_types, array_c_types)
        # MIDDLE ROWS
        else:
            # start with edge
            result_array, result_array_types, array_e, array_e_types = get_match("vertical", result_array, array_e, result_array_types, array_e_types)

            # start with a middle that matches with the other one
            for j in range(column - 2):
                # match piece with left piece
                result_array, result_array_types, array_m, array_m_types = get_match("horizontal", result_array, array_m, result_array_types, array_m_types)

            # end with edge
            result_array, result_array_types, array_e, array_e_types = get_match("horizontal", result_array, array_e, result_array_types, array_e_types)

    return result_array


def get_match(direction, result_array, array_border, result_array_types, array_border_types):
    print("-----------new match-----------")
    matches = []
    means = []
    total_rotated_numbers = []
    smallest_mean = 1000
    index = 0
    global column
    global method_used
    for k in range(len(array_border)):
        if direction == "horizontal":
            match, mean, total_rotated = match_horizontal(method_used, result_array[len(result_array) - 1], array_border[k], result_array_types[len(result_array_types) - 1], array_border_types[k])
        if direction == "vertical":
            match, mean, total_rotated = match_vertical(method_used, result_array[len(result_array) - column], array_border[k], result_array_types[len(result_array_types) - column], array_border_types[k])
        matches.append(match)
        means.append(mean)
        total_rotated_numbers.append(total_rotated)
        # print(array_border_types[k])
        # cv2.imshow("image", array_border[k])
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        if mean < smallest_mean and match is True:
            smallest_mean = mean
            index = k

    print("Find one match of these: ")
    print(matches)
    print(means)
    print(total_rotated_numbers)
    if method_used != "shuffled":
        for i in range(total_rotated_numbers[index] + 1):
            array_border[index], array_border_types[index] = rotate_image(array_border[index], array_border_types[index], 90)
    # print(array_border_types[index])
    # print(array_border_types)

    if matches[index] and means[index] == smallest_mean:
        print("match added")
        result_array.append(array_border[index])
        result_array_types.append(array_border_types[index])
        remove_array(array_border, array_border[index])
        # array_border_types.remove(array_border_types[index])
        # remove_array(array_border_types, array_border_types[index])
        del array_border_types[index]

    # print(array_border_types)
    # print_array(array_border)
    # print(array_border_types[index])
    # cv2.imshow("image", array_border[index])
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return result_array, result_array_types, array_border, array_border_types


def remove_array(L, arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind], arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        raise ValueError('array not found in list.')
