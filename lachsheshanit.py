def read_image(path_to_image: str):
    """
    A function gets a path to an image, reads the bits in the image and finds correct words.
    :param path_to_image: path to crypto-image
    :return: None
    """
    str_result = ""
    try:
        with open(path_to_image, "rb") as image_file:
            byte = image_file.read(1)
            while byte:
                byte_hex = int(byte.hex(), 16)
                if byte_hex in range(97, 123):
                    str_result += chr(byte_hex)

                elif byte_hex == 33:
                    str_result += chr(byte_hex)
                    if len(str_result) > 6:
                        print(str_result)
                        str_result = ""
                else:
                    str_result = ""
                byte = image_file.read(1)
    except IOError:
        print('Error While Opening the file!')


def main():
    read_image("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\logo.jpg")


if __name__ == '__main__':
    main()
    