import math
import time


def average_runtime(words):
    timeFirst = time.time()
    for i in range(0, 1000):
        if "zwitterion" in words:
             continue
    timeSecond = time.time()
    return (timeSecond - timeFirst) / 1000


word_list = []
word_set = set()

try:
    with open("words.txt", "r") as f:
        word = f.readline(1)
        while word:
            word_list.append(word)
            word_set.add(word)
            word = f.readline(1)
except IOError:
    print('Error While Opening the file!')


print(f"The time for find zwitterion in list: {average_runtime(word_list)}")
print(f"The time for find zwitterion in set: {average_runtime(word_set)}")

"""
The time for find zwitterion in list: 0.07697811603546142
The time for find zwitterion in set: 0.0
"""



