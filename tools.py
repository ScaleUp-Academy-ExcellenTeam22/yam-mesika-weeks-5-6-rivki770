def interleave(*iterable):
    """
     A function that receives a list of lists and returns a merge between the lists
    :param iterable: Unlimited list of objects.
    :return: In each reading the object in the next position
    """
    size_min = min(len(i) for i in iterable)

    current_number = 0
    while current_number < size_min:
        for i in iterable:              # move on all a list
            yield i[current_number]
        current_number += 1


def main():
    #example_1
    print([p for p in interleave('abc', [1, 2, 3], ('!', '@', '#'))])

    #example_2
    print([p for p in interleave('abc', [1, 2], ('!', '@', '#'))])

    #example_3
    print([p for p in interleave('abc', [1, 2, 3], ('!', '@', '#'), 'XYZ')])


if __name__ == '__main__' :
    main()
