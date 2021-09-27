SOURCE_IMAGE = 'input_images/374284-overlord3_super.jpg'


def writing_note():
    with open(SOURCE_IMAGE, 'ab') as f:
        f.write(b'Abandon all hope ye who enter here')
    return None


def reading_note():
    with open(SOURCE_IMAGE, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        print(f.read())
    return None


if __name__ == '__main__':
    # writing_note()
    reading_note()
