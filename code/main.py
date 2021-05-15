import cv2
import winsound
import argparse
from extraction_original import extract_parameters
from segmentation import segment_image
from extraction_single_image import search_borders, get_smallest_shape_scrambled
from solution import solve_puzzle
from result import *
from matching import *


# play background sound
winsound.PlaySound("test.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)


def main(image_name):
    image = cv2.imread(image_name)
    total_pieces, method, type = extract_parameters(image_name, image)
    all_array = segment_image(image, total_pieces, method, type)
    # print_array(all_array)
    border_types = search_borders(all_array)
    array_c, array_e, array_m, array_c_types, array_e_types, array_m_types = sort_images(all_array, border_types)
    print("containers with borders")
    # print_array(array_c)
    print(array_c_types)
    print("--------")
    # print_array(array_e)
    print(array_e_types)
    print("----------")
    # print_array(array_m)
    print(array_m_types)
    print("----------")
    result_array = solve_puzzle(total_pieces, method, array_c, array_e, array_m, array_c_types, array_e_types, array_m_types)
    # print_array(result_array)
    length, width = get_smallest_shape_scrambled(result_array)
    final_image = show_puzzle(total_pieces, length, width, result_array)
    return final_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Project multimedia')
    parser.add_argument("--method",
                        help="method name: (shuffled, rotated, scrambled)",
                        default="shuffled")
    parser.add_argument('--dataset', help='dataset name: (2x2, 2x3, 3x3, 4x4, 5x5)', default="2x2")
    args = parser.parse_args()
    name = "images/jigsaw_" + args.method + "/jigsaw_" + args.method + "_" + args.dataset + "_0"
    for i in range(9):
        i = str(i)
        print("puzzle" + i)
        try:
            image = main(name + i + ".png")
            cv2.imshow("puzzle" + i, image)
        except:
            print("Program failed, possibly wrong method name or dataset name")
        print("--------------------------------------------------------")
    winsound.PlaySound(None, winsound.SND_ASYNC)     # adding winning music
    add_music()
    cv2.waitKey()
    cv2.destroyAllWindows()
