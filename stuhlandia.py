def state_in_line_on_keyboard(path_to_file_of_country: str):
    """
    A function that gets a path to a file with countries,
    looks for a country that can type in one line on the keyboard.
    :param path_of_file_of_country: path to file of states.
    :return: nothing.
    """
    first_keyboard_row = set('qwertyuiop\n')
    second_keyboard_row = set('asdfghjkl\n')
    third_keyboard_row = set('zxcvbnm\n')

    try:
        with open(path_to_file_of_country, "r") as file_country:
            state = file_country.readline()
            while state:
                start_set = set(state)
                if len(set(start_set.difference(first_keyboard_row))) == 0:
                    print(f'In row 1: {state}')
                    return
                elif len(set(start_set.difference(second_keyboard_row))) == 0:
                    print(f'In row 2: {state}')
                    return
                elif len(set(start_set.difference(third_keyboard_row))) == 0:
                    print(f'In row 3: {state}')
                    return
                state = file_country.readline()
    except IOError:
        print('Error While Opening the file!')


def main():
    state_in_line_on_keyboard("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\states.txt")


if __name__ == '__main__' :
    main()
