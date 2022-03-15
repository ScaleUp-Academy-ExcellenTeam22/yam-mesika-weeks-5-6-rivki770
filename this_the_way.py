import os


def rename_files(path):
    list_of_file = os.listdir(path)
    for entry in list_of_file:
        if "deep" in entry[0:4]:
            print(entry)


rename_files("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\images")