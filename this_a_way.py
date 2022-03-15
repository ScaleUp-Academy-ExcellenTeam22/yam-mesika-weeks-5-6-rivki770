import os

def deep_files(path):
    list_of_file = os.listdir(path)
    all_files = []
    for entry in list_of_file:
        if 'deep' == entry[0:4]:
            all_files.append(entry)
    return all_files


list_file = deep_files("C:\\rivki\\studies\\YearD\\SemesterB\\Excellent\\Python\\HW_1\\Git\\yam-mesika-weeks-5-6-rivki770\\images")
for file in list_file:
    print(file)