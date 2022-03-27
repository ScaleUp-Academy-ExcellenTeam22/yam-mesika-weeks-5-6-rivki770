import math
import time


def average_runtime(words):
    """
    A function that receives a list of words and returns how long it takes on average to search for a specific word.
    :param words: or set of words or list of words
    :return: the average-time to find "zwitterion" in a set or a list
    """
    time_first = time.time()
    for i in range(0, 1000):
        if "zwitterion" in words:
             continue
    time_second = time.time()
    return (time_second - time_first) / 1000


def open_file(path_to_file: str):
    """
    A function that gets a path to a file, and copy the line from a file to list and set,
    and she call to inner function.
    :param path_to_file: path to file.
    :return: nothing.
    """
    word_list = []
    word_set = set()

    try:
        with open(path_to_file, "r") as file:
            word = file.readline(1)
            while word:
                word_list.append(word)
                word_set.add(word)
                word = file.readline(1)
    except IOError:
        print('Error While Opening the file!')

    print(f"The time for find zwitterion in list: {average_runtime(word_list)}")
    print(f"The time for find zwitterion in set: {average_runtime(word_set)}")


def main():
    open_file("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\words.txt")


if __name__ == '__main__':
    main()
