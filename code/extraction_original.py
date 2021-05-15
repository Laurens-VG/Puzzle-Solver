from segmentation import get_rectangles


def extract_parameters(image_name, image):
    if image_name.find("tiles") != -1:
        type = "tiles"
    if image_name.find("jigsaw") != -1:
        type = "jigsaw"
    if image_name.find("rotated") != -1:
        method = "rotated"
    if image_name.find("scrambled") != -1:
        method = "scrambled"
    if image_name.find("shuffled") != -1:
        method = "shuffled"
    if type == "jigsaw":
        total_pieces = len(get_rectangles(image))
    print(total_pieces)
    print(method)
    print(type)
    return total_pieces, method, type



