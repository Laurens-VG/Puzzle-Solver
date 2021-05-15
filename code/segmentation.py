import cv2
import random as rng
import numpy as np
import imutils
from copy import deepcopy
from result import print_array


def segment_image(image, total_pieces, method, type):
    rectangles = get_rectangles(image)
    if type == "tiles":
        if method == "shuffled" or method == "rotated":
            all_array = cut_tiles(image, total_pieces)
        elif method == "scrambled":
            all_array = cut_image_rectangles(image, rectangles)
        else:
            print("No method selected")
    elif type == "jigsaw":
        all_array = cut_image_rectangles(image, rectangles)
        if method == "scrambled":
            for i in range(len(all_array)):
                all_array[i] = rotate_scrambled(all_array[i], 1)
                # all_array[i] = scrambled_angle(all_array[i])
    else:
        print("No type selected")
    return all_array


def get_rectangles(image):
    rectangles = []
    image = sobel(image)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
    drawing = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0, 256), rng.randint(0, 256), rng.randint(0, 256))
        cv2.drawContours(drawing, contours_poly, i, color)
        p1 = (int(boundRect[i][0]), int(boundRect[i][1]))
        p2 = (int(boundRect[i][0] + boundRect[i][2]), int(boundRect[i][1] + boundRect[i][3]))
        if boundRect[i][2] > 50:
            cv2.rectangle(drawing, p1, p2, color, 2)
            rectangles.append([p1, p2])
    # cv2.imshow("image", drawing)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return rectangles


def cut_image_rectangles(image, rectangles):
    all_array = []
    for i in range(len(rectangles)):
        all_array.append(deepcopy(image[rectangles[i][0][1]: rectangles[i][1][1]: 1, rectangles[i][0][0]: rectangles[i][1][0]: 1, :]))
    return all_array


def cut_tiles(image, total_pieces):
    all_array = []
    length = image.shape[0]
    width = image.shape[1]
    if total_pieces == 4:
        piece1 = deepcopy(image[: int(length / 2): 1, : int(width / 2): 1, :])
        all_array.append(piece1)
        piece2 = deepcopy(image[int(length / 2):: 1, : int(width / 2): 1, :])
        all_array.append(piece2)
        piece3 = deepcopy(image[: int(length / 2): 1, int(width / 2):: 1, :])
        all_array.append(piece3)
        piece4 = deepcopy(image[int(length / 2):: 1, int(width / 2):: 1, :])
        all_array.append(piece4)
    return all_array


def sobel(I):
    I = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
    grad_x = cv2.Sobel(I, cv2.CV_16S, 1, 0)
    grad_y = cv2.Sobel(I, cv2.CV_16S, 0, 1)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad


def rotate_scrambled(image, shape):
    length = image.shape[shape]
    new_angle = 0
    for angle in np.arange(0, 360, 1):
        new_image = imutils.rotate_bound(image, angle)  # ndimage.rotate
        rect = get_rectangles(new_image)
        array = cut_image_rectangles(new_image, rect)
        if array[0].shape[shape] < length:
            length = array[0].shape[shape]
            new_angle = angle
        # cv2.imshow("Final", array[0])
        # cv2.waitKey(0)
    print("angle:", new_angle)
    new_image = imutils.rotate_bound(image, new_angle)
    rect = get_rectangles(new_image)
    array = cut_image_rectangles(new_image, rect)
    # cv2.imshow("Final rotated", array[0])
    # cv2.waitKey()
    return array[0]