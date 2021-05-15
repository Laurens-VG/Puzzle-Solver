import cv2
import winsound
from main import main
from result import *

if __name__ == "__main__":
    # play background sound
    winsound.PlaySound("test.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_05.png"
    image = main(name)
    cv2.imshow("puzzle 2x2", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x3_03.png"
    image = main(name)
    cv2.imshow("puzzle 2x3", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_3x3_02.png"
    image = main(name)
    cv2.imshow("puzzle 3x3", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_06.png"
    image = main(name)
    cv2.imshow("puzzle 4x4", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_01.png"
    image = main(name)
    cv2.imshow("puzzle_2 4x4", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_04.png"
    image = main(name)
    cv2.imshow("puzzle_1 5x5 ", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_00.png"
    image = main(name)
    cv2.imshow("puzzle_2 5x5", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_07.png"
    image = main(name)
    cv2.imshow("puzzle_3 5x5", image)

    method = "shuffled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_08.png"
    image = main(name)
    cv2.imshow("puzzle_4 5x5", image)


    winsound.PlaySound(None, winsound.SND_ASYNC)  # adding winning music
    add_music()
    cv2.waitKey()
    cv2.destroyAllWindows()

    # play background sound
    winsound.PlaySound("test.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_01.png"
    image = main(name)
    cv2.imshow("puzzle 2x2", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x3_03.png"
    image = main(name)
    cv2.imshow("puzzle 2x3", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_3x3_06.png"
    image = main(name)
    cv2.imshow("puzzle 3x3", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_07.png"
    image = main(name)
    cv2.imshow("puzzle_1 4x4", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_00.png"
    image = main(name)
    cv2.imshow("puzzle_2 4x4", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_02.png"
    image = main(name)
    cv2.imshow("puzzle_3 4x4", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_05.png"
    image = main(name)
    cv2.imshow("puzzle_1 5x5", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_08.png"
    image = main(name)
    cv2.imshow("puzzle_2 5x5", image)

    method = "rotated"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_5x5_04.png"
    image = main(name)
    cv2.imshow("puzzle_3 5x5", image)


    winsound.PlaySound(None, winsound.SND_ASYNC)  # adding winning music
    add_music()
    cv2.waitKey()
    cv2.destroyAllWindows()

    # play background sound
    winsound.PlaySound("test.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_01.png"
    image = main(name)
    cv2.imshow("puzzle_1 2x2", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_02.png"
    image = main(name)
    cv2.imshow("puzzle_2 2x2", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_04.png"
    image = main(name)
    cv2.imshow("puzzle_3 2x2", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x2_07.png"
    image = main(name)
    cv2.imshow("puzzle_4 2x2", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x3_08.png"
    image = main(name)
    cv2.imshow("puzzle_1 2x3", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x3_00.png"
    image = main(name)
    cv2.imshow("puzzle_2 2x3", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_2x3_06.png"
    image = main(name)
    cv2.imshow("puzzle_3 2x3", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_3x3_05.png"
    image = main(name)
    cv2.imshow("puzzle_1 3x3", image)

    method = "scrambled"
    name = "images/jigsaw_" + method + "/jigsaw_" + method + "_3x3_03.png"
    image = main(name)
    cv2.imshow("puzzle_2 3x3", image)

    # method = "scrambled"
    # name = "images/jigsaw_" + method + "/jigsaw_" + method + "_4x4_08.png"
    # image = main(name)
    # cv2.imshow("puzzle 4x4", image)

    winsound.PlaySound(None, winsound.SND_ASYNC)  # adding winning music
    add_music()
    cv2.waitKey()
    cv2.destroyAllWindows()