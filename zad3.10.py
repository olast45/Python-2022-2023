dict1 = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

dict2 = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arab = [1, 5, 10, 50, 100, 500, 1000]

dict3 = dict(zip(roman, arab))


# print(dict1)
# print(dict2)
# print(dict3)


def roman2int(string_roman):
    i = 0
    result = 0
    roman2arab = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    while i < len(string_roman):
        num1 = roman2arab[string_roman[i]]
        if (i + 1) < len(string_roman):
            num2 = roman2arab[string_roman[i+1]]
            if num1 < num2:
                result += (num2-num1)
                i += 2
            else:
                result += num1
                i += 1
        else:
            result += num1
            i += 1

    return result


print(roman2int('MMCDX'))


