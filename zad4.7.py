def flatten(sequence):
    flatten_list = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flatten_list.extend(flatten(item))
            # print(flatten_list)
        else:
            flatten_list.append(item)
            # print(flatten_list)
            # print(item)

    # print(flatten_list)
    return flatten_list


seq = [1, 2, [3, 1, [0]], 7, [1, [5, 3, [4, (1, 2)]], 9, 2], 1, (8, 9)]
result = flatten(seq)
print(result)