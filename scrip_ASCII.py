from PIL import Image

# ASCII_CHARS = [x+1 for x in range(10)]
# ASCII_CHARS.extend([',', '.', '+', '-', '*'])
ASCII_CHARS = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]


def resize_image(image: Image, new_width: int) -> Image:
    """
    Change size of input img file.

    :param image: Image class instance,
    :param new_width: int type,
    :return: Image class instance.
    """

    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.35)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def gray_out(image: Image) -> Image:
    """
    Return input bitmap into gray palette.

    :param image: Image class instance,
    :return: Image class instance.
    """

    grayscale_image = image.convert('L')
    return grayscale_image


def pixels_to_ascii(image: Image) -> str:
    """
    Generate str value by using global var ASCII_CHARS containing list of ASCII characters.

    :param image: Image class instance,
    :return: str value containing ASCII image.
    """
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def main(new_width: int = 800) -> None:
    """
    Ask for path of input file.
    Call right sequence of previous defined functions,
    Split str value into rows,
    Save new .txt file in input file folder.

    :param new_width: int type, try change basic 800 value to rewrite size of image,
    :return: None
    """

    path = input('Enter patch to image: ')
    image = Image.open(path)

    new_image_data = pixels_to_ascii(gray_out(resize_image(image, new_width)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)

    with open(str(str(path[:-4]) + ".txt"), 'w') as f:
        f.write(ascii_image)

    return None


if __name__ == '__main__':
    main()
