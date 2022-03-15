def join(*list_param, sep="-"):
    if len(list_param) == 0:
        return None

    list_new = []
    for param in list_param:
        list_new += param
        list_new.append(sep)
    list_new.pop()
    return list_new


def main():
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())


if __name__ == '__main__' :
    main()