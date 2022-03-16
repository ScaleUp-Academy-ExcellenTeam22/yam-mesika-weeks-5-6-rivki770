import os
import re
import codecs


def rename_files(path):
    list_of_file = os.listdir(path)
    for entry in list_of_file:
        full_path = os.path.join(path, entry)
        codecs.register_error("strict", codecs.ignore_errors)
        f = codecs.open(full_path, 'r').read()
        match = re.search('<title>(.*?)</title>', f)
        title = match.group(1)
        title = title.split("Chapter ")  #we get title[o] = before chapter, title[1] = after chapter
        title = title[1].split(":")  #we get title[o] = a number, title[1] = a title

        title[0] = title[0].zfill(3) #conver the number to number with 3 digits

        full_path_new = os.path.join(path, title[0] + title[1] + ".html")
        os.rename(full_path, full_path_new)


list_file = rename_files("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\potter")