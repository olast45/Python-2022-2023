def sum_sequence(sequence):
    res = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            res += sum_sequence(item)
            # print(item)
            # print('\n')
        else:
            res += item
            # print(item)
    return res


seq = [1, 2, [3, 1, [0]], 7, [1, [5, 3, [4, (1, 2)]], 9, 2], 1, (8, 9)]
result = sum_sequence(seq)
print(result)





