import PIL.Image
import io
import os


VISIBLE_IMAGE = 'input_images/bandyta_d.jpg'
HIDDEN_IMAGE = 'input_images/demonolog.gif'


def hide_image():
    image = PIL.Image.open(HIDDEN_IMAGE)
    byte_arr = io.BytesIO()
    image.save(byte_arr, format='GIF')

    with open(VISIBLE_IMAGE, 'ab') as f:
        f.write(byte_arr.getvalue())

    return None


def unhide_image():
    with open(VISIBLE_IMAGE, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        
        f.seek(offset + 2)
        new_image = PIL.Image.open(io.BytesIO(f.read()))
        new_image.save(VISIBLE_IMAGE[:-4] + '.gif')

    # os.remove(VISIBLE_IMAGE)

    return None


if __name__ == '__main__':
    # hide_image()
    unhide_image()
