import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from matching import get_pixelvalue_black_sides


def search_borders(array):
    length, width = get_smallest_shape_scrambled(array)
    # length, width = get_smallest_shape(array)
    array_of_plots = []
    array_of_avg_plots = []
    array_of_borders_kind = []
    array_of_borders_type = []
    cst = 15
    total_female = 0
    total_male = 0
    for i in range(len(array)):
        # Get plot of distance to borders of image
        image_middle, corners = get_middle_of_image(array[i], length, width)
        plot, plot0, plot1, plot2, plot3 = get_distance_of_image(array[i], image_middle, corners)
        array_of_plots.append(plot)

        # Get angled or straight borders (kind)
        borders_kind = get_borders_kind(plot0, plot1, plot2, plot3, length, width)
        array_of_borders_kind.append(borders_kind)

        # Get avg plot of distance to borders of image
        avg_plot, avg_plot0, avg_plot1, avg_plot2, avg_plot3 = get_average_distance_of_image(corners[0], corners[3])
        avg_plot, avg_plot0, avg_plot1, avg_plot2, avg_plot3 = concatenate_avg_plots(borders_kind, avg_plot0, plot0, avg_plot1, plot1,  avg_plot2, plot2, avg_plot3, plot3)
        array_of_avg_plots.append(avg_plot)
        # plot_axis = np.arange(len(avg_plot))
        # plt.plot(plot_axis, avg_plot)
        # plt.show()

        # Get female or male borders (type)
        borders_type = get_borders_type(plot0, plot1, plot2, plot3, avg_plot0, avg_plot1, avg_plot2, avg_plot3, cst)

        # Compare borders
        got_wrong_borders = False
        for j in range(4):
            if borders_kind[j] == "S" and borders_type[j] != "S":
                borders_type[j] = "S"
            if borders_kind[j] == "A" and borders_type[j] == "S":
                got_wrong_borders = True

        while got_wrong_borders:
            cst -= 1
            # print(cst)
            teller = 0
            borders_type = get_borders_type(plot0, plot1, plot2, plot3, avg_plot0, avg_plot1, avg_plot2, avg_plot3, cst)
            for j in range(len(borders_type)):
                if borders_kind[j] == "S" and borders_type[j] != "S":
                    borders_type[j] = "S"
                if borders_kind[j] == "A" and borders_type[j] == "S":
                    teller += 1
            if teller == 0:
                got_wrong_borders = False
            else:
                got_wrong_borders = True

        # Get total female and male
        for j in range(4):
            if borders_type[j] == "F":
                total_female += 1
            elif borders_type[j] == "M":
                total_male += 1
        cst = 15
        array_of_borders_type.append(borders_type)

    print(total_female)
    print(total_male)
    print(array_of_borders_kind)
    print(array_of_borders_type)

    return array_of_borders_type


def get_smallest_shape_scrambled(array):
    # cv2.imshow("d", array[0])
    # cv2.waitKey()
    black_u, black_l, black_d, black_r = get_pixelvalue_black_sides(array[0])
    black_d -= 2
    black_u -= 2
    black_l -= 2
    black_r -= 2
    length = array[0].shape[0] - black_u - black_d
    width = array[0].shape[1] - black_l - black_r
    # print(length)
    # print(width)
    return length, width


def get_middle_of_image(image, length, width):
    black_u, black_l, black_d, black_r = get_pixelvalue_black_sides(image)
    black_d -= 2
    black_u -= 2
    black_l -= 2
    black_r -= 2
    mid_width = round(width/2)
    mid_length = round(length/2)
    image_middle = (mid_width + black_l, mid_length + black_u)
    # get corners
    corner1 = image_middle[0] + round(width / 2), image_middle[1] + round(length / 2)  # Right down
    corner2 = image_middle[0] - round(width / 2), image_middle[1] + round(length / 2)  # Right up
    corner3 = image_middle[0] + round(width / 2), image_middle[1] - round(length / 2)  # Left down
    corner4 = image_middle[0] - round(width / 2), image_middle[1] - round(length / 2)  # Left up
    corners = [corner1, corner2, corner3, corner4]
    # print circles
    # cv2.circle(image, image_middle, 5, (0, 255, 0))
    # cv2.circle(image, corner1, 5, (0, 255, 0))
    # cv2.circle(image, corner2, 5, (255, 0, 0))
    # cv2.circle(image, corner3, 5, (0, 0, 255))
    # cv2.circle(image, corner4, 5, (255, 255, 255))
    return image_middle, corners


def calculate_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def get_distance_of_image(image, image_middle, corners):
    p1 = corners[0]  # right down
    p2 = corners[1]  # left down
    p3 = corners[2]  # right up
    p4 = corners[3]  # left up
    min_distance_to_corner = 6  # HARDCODED
    plot = []
    plot0 = []
    plot1 = []
    plot2 = []
    plot3 = []
    plot4 = []
    counter = 0
    # image = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    # # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # # drawing = cv2.morphologyEx(drawing, cv2.MORPH_CLOSE, kernel)
    # for i in range(len(contours)):
    #     cv2.drawContours(drawing, contours, i, (0, 255, 255))
    # cv2.imshow("im", drawing)
    # cv2.waitKey()
    # print(len(contours))
    # p = contours[0][10][0][0], contours[0][10][0][1]
    # cv2.circle(image, p, 25, (255, 0, 0))  # First contour point

    for i in range(len(contours[0])):
        p = contours[0][i][0][0], contours[0][i][0][1]
        if calculate_distance(p[0], p[1], p4[0], p4[1]) < min_distance_to_corner:
            counter = 1
            # print("left up")
        elif calculate_distance(p[0], p[1], p2[0], p2[1]) < min_distance_to_corner:
            counter = 2
            # print("left down")
        elif calculate_distance(p[0], p[1], p1[0], p1[1]) < min_distance_to_corner:
            counter = 3
            # print("right down")
        elif calculate_distance(p[0], p[1], p3[0], p3[1]) < min_distance_to_corner:
            counter = 4
            # print("right up")
        # print(counter)
        if counter == 0:
            plot0.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
            plot.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
        if counter == 1:
            plot1.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
            plot.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
        if counter == 2:
            plot2.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
            plot.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
        if counter == 3:
            plot3.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
            plot.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
        if counter == 4:
            plot4.append(calculate_distance(p[0], p[1], image_middle[0], image_middle[1]))
        # cv2.circle(image, p, 5, (0, 255, 0))
    for i in range(len(plot4)):
        plot0.insert(i, plot4[i])
        plot.insert(i, plot4[i])
    # plot and show
    # plot_distance_of_image(plot0, plot1, plot2, plot3)
    # cv2.imshow("image", image)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return plot, plot0, plot1, plot2, plot3


def plot_distance_of_image(plot0, plot1, plot2, plot3):
    plot0_axis = np.arange(len(plot0))
    plot1_axis = np.arange(len(plot0), len(plot0) + len(plot1))
    plot2_axis = np.arange(len(plot0) + len(plot1), len(plot0)+len(plot1)+len(plot2))
    plot3_axis = np.arange(len(plot0) + len(plot1) + len(plot2), len(plot0)+len(plot1)+len(plot2)+len(plot3))
    plt.plot(plot0_axis, plot0, color='b')
    plt.plot(plot1_axis, plot1, color='g')
    plt.plot(plot2_axis, plot2, color='r')
    plt.plot(plot3_axis, plot3, color='c')
    plt.show()


def get_average_distance_of_image(p1, p2):
    length = p1[1]-p2[1]
    width = p1[0]-p2[0]
    middle = length/2, width/2
    plot = []
    contours = []
    for i in range(width):
        p = width-i, 0
        contours.append(p)
    for j in range(1, length):
        p = 0, j
        contours.append(p)
    for k in range(width):
        p = k, length
        contours.append(p)
    for l in range(length):
        p = width, length-l
        contours.append(p)
    for p in range(len(contours)):
        plot.append(calculate_distance(contours[p][0], contours[p][1], middle[1], middle[0]))
    avg_plot0 = plot[0: width]
    avg_plot1 = plot[width: width + length]
    avg_plot2 = plot[width + length:width + length + width]
    avg_plot3 = plot[width + length + width: width + length + width + length]
    return plot, avg_plot0, avg_plot1, avg_plot2, avg_plot3


def concatenate_avg_plots(borders, avg_plot0, plot0,  avg_plot1, plot1, avg_plot2, plot2,  avg_plot3, plot3):
    # print(borders)
    angled_sides = [i for i, x in enumerate(borders) if x == 'A']
    # print(angled_sides)
    for i in range(len(angled_sides)):
        if angled_sides[i] == 0:
            avg_plot0 = stretch_array(plot0, avg_plot0)
        if angled_sides[i] == 1:
            avg_plot1 = stretch_array(plot1, avg_plot1)
        if angled_sides[i] == 2:
            avg_plot2 = stretch_array(plot2, avg_plot2)
        if angled_sides[i] == 3:
            avg_plot3 = stretch_array(plot3, avg_plot3)
    avg_plot = np.concatenate((avg_plot0, avg_plot1, avg_plot2, avg_plot3))
    return avg_plot, avg_plot0, avg_plot1, avg_plot2, avg_plot3


def stretch_array(array1, array2):
    # print(len(array1))
    # print(len(array2))
    if len(array1) > len(array2):
        diff_length = int(len(array1) - len(array2))
        interval = int(len(array1) / diff_length)
        new = 0
        for i in range(diff_length):
            array2.insert(new, array2[new])
            new += interval
    return array2


def get_borders_kind(plot0, plot1, plot2, plot3, length, width):
    cst = 8  # HARDCODED
    upper_border = "S"
    left_border = "S"
    lower_border = "S"
    right_border = "S"
    diffs = len(plot0) - width
    # print(diffs)
    if diffs > cst:
        upper_border = "A"
    diffs = len(plot1) - length
    # print(diffs)
    if diffs > cst:
        left_border = "A"
    diffs = len(plot2) - width
    # print(diffs)
    if diffs > cst:
        lower_border = "A"
    diffs = len(plot3) - length
    # print(diffs)
    if diffs > cst:
        right_border = "A"
    borders = [upper_border, left_border, lower_border, right_border]
    # print(borders)
    return borders


def get_borders_type(plot0, plot1, plot2, plot3, avg_plot0, avg_plot1, avg_plot2, avg_plot3, cst):
    #  cst = 15  # HARDCODED
    upper_border = "S"
    left_border = "S"
    lower_border = "S"
    right_border = "S"
    for i in range(10, len(avg_plot0) - 10):
        diffs = plot0[i] - avg_plot0[i]
        # print(diffs)
        if diffs > cst:
            upper_border = "M"
        elif diffs < -cst:
            upper_border = "F"
    # print(upper_border)
    # print("--------------------")
    for i in range(10, len(avg_plot1) - 10):
        diffs = plot1[i] - avg_plot1[i]
        # print(diffs)
        if diffs > cst:
            left_border = "M"
        elif diffs < -cst:
            left_border = "F"
    # print(left_border)
    # print("--------------------")
    for i in range(10, len(avg_plot2) - 10):
        diffs = plot2[i] - avg_plot2[i]
        # print(diffs)
        if diffs > cst:
            lower_border = "M"
        elif diffs < -cst:
            lower_border = "F"
    # print("--------------------")
    for i in range(10, len(avg_plot3) - 10):
        diffs = plot3[i] - avg_plot3[i]
        # print(diffs)
        if diffs > cst:
            right_border = "M"
        elif diffs < -cst:
            right_border = "F"
    # plot_axis = np.arange(len(plot3))
    # plt.plot(plot_axis, plot3)
    # plot_axis2 = np.arange(len(avg_plot3))
    # plt.plot(plot_axis2, avg_plot3)
    # plt.show()
    borders = [upper_border, left_border, lower_border, right_border]
    # print(borders)
    return borders
