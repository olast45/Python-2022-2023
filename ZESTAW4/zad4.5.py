def reverse_iter(ls, left, right):
    sublist = []
    for i in range(left, right+1):
        sublist.append(ls[i])
        # print(ls[i])

    sublist.reverse()
    ls[left:right+1] = sublist[:]

    return ls


def reverse_rec(ls, left, right):
    if left >= right:
        return
    else:
        temp = ls[left]
        ls[left] = ls[right]
        ls[right] = temp
        reverse_rec(ls, left + 1, right-1)
    return ls


x = input('''Wybierz czy chcesz wykonac zadanie w sposob iteracyjny czy rekurencyjny\nJeżeli w iteracyjny wpisz "i", 
natomiast jeśli w rekurencyjny wpisz "r": ''')


list_to_reverse = [1, 4, 5, 2, 0, 7, 9, 10]
start_index = 2
end_index = 6

if x == 'i':
    result = reverse_iter(list_to_reverse, start_index, end_index)
    print(result)

elif x == 'r':
    result = reverse_rec(list_to_reverse, start_index, end_index)
    print(result)

else:
    print('Wybrano niepoprawną opcję!')
