import os
import re
import codecs


def rename_files(path_to_files):
    """
    A function that gets a path to a list of files, and renames the file according to the content.
    :param path_to_files: path to a list of files.
    :return: nothing
    """
    list_of_files = os.listdir(path_to_files)
    for one_file in list_of_files:
        full_path = os.path.join(path_to_files, one_file)
        codecs.register_error("strict", codecs.ignore_errors)
        file = codecs.open(full_path, 'r').read()
        match = re.search('<title>(.*?)</title>', file)
        title = match.group(1)
        title = title.split("Chapter ")  # we get title[o] = before chapter, title[1] = after chapter
        title = title[1].split(":")  # we get title[o] = a number, title[1] = a title

        title[0] = title[0].zfill(3) # conver the number to number with 3 digits

        full_path_new = os.path.join(path_to_files, title[0] + title[1] + ".html")
        os.rename(full_path, full_path_new)


def main():
    rename_files("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\potter")


if __name__ == '__main__':
    main()
