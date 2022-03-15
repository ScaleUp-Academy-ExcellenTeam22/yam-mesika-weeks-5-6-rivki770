def interleave(*iterable):
    size_min = 200
    for i in iterable:
        if len(i) < size_min:
            size_min = len(i)

    current_number = 0
    while current_number < size_min:
        for i in iterable:
            yield i[current_number]
        current_number = current_number + 1


def main():
    #example_1
    arr = []
    pointer = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for p in pointer:
        arr.append(p)
    print(arr)

    #example_2
    arr = []
    pointer = interleave('abc', [1, 2], ('!', '@', '#'))
    for p in pointer:
        arr.append(p)
    print(arr)

    #example_3
    arr = []
    pointer = interleave('abc', [1, 2, 3], ('!', '@', '#'), 'XYZ')
    for p in pointer:
        arr.append(p)
    print(arr)



if __name__ == '__main__' :
    main()