def make_ruler(length):

    ruler = ('|....' * (length - 1)) + '|'
    begin = '0'

    for i in range(1, length):
        num = len(str(i))
        begin += ' ' * (5 - num)
        begin += f"{i}"

    result = ruler + '\n' + begin
    return result


def make_grid(height, length):
    result = ""
    for i in range(height + 1):
        top = ("*---" * length) + "*"
        result += (top + "\n")
        bottom = "|   " * length + "|"
        if i != height:
            result += bottom + "\n"
    return result


ruler_length = 12
grid_length = 4
grid_height = 2

res = make_ruler(ruler_length)
print(res)

res2 = make_grid(grid_height, grid_length)
print(res2)