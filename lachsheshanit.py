def main():
    str_result = ""
    try:
        with open("logo.jpg", "rb") as f:
            byte = f.read(1)
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
                byte = f.read(1)
    except IOError:
        print('Error While Opening the file!')


if __name__ == '__main__' :
    main()