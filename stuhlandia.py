row1 = set('qwertyuiop\n')
row2 = set('asdfghjkl\n')
row3 = set('zxcvbnm\n')

try:
    with open("states.txt", "r") as f:
        state = f.readline()
        while state:
            start_set = set(state)
            if len(set(start_set.difference(row1))) == 0:
                print(f'In row 1: {state}')
                break
            elif len(set(start_set.difference(row2))) == 0:
                print(f'In row 2: {state}')
                break
            elif len(set(start_set.difference(row3))) == 0:
                print(f'In row 3: {state}')
                break
            state = f.readline()
except IOError:
    print('Error While Opening the file!')