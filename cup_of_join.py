def join_lists_to_one_list(*lists_param: list, sep="-") -> list:
    """
    A function that consolidates an unlimited number of lists into one list,
    with a separator character between the lists.
    :param lists_param: Unlimited amount of lists.
    :param sep: separation character between lists.
    :return: consolidated_list: A consolidated list from all the lists.
    """
    if len(lists_param) == 0:
        return []

    for inner_list in lists_param:
        inner_list.append(sep)

    consolidated_list = [char for inner_list in lists_param for char in inner_list]
    consolidated_list.pop()
    return consolidated_list


def main():
    print(join_lists_to_one_list([1, 2], [8], [9, 5, 6], sep='@'))
    print(join_lists_to_one_list([1, 2], [8], [9, 5, 6]))
    print(join_lists_to_one_list([1]))
    print(join_lists_to_one_list())


if __name__ == '__main__' :
    main()
