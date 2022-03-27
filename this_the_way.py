import os


def files_starts_at_deep(path_to_files_folder: str):
    """
    The function check which files in the folder start in deep.
    :param path_to_files_folder: The path to folder
    :return: list of a files that they start in deep.
    """
    list_of_file = os.listdir(path_to_files_folder)
    list_file_deep = [file for file in list_of_file if file.startswith('deep')]
    return list_file_deep


def main():
    print(files_starts_at_deep("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\images"))


if __name__ == '__main__':
    main()