# A
def common_elements(el1, el2):
    el1_set = set(el1)
    el2_set = set(el2)

    if el1_set & el2_set:
        print(list(el1_set & el2_set))
    else:
        print('Te dwie sekwencje nie mają wspólnych elementów!')


# B
def all_elements(el1, el2):
    el1_set = set(el1)
    el2_set = set(el2)
    print(list(el1_set | el2_set))


numbers1 = [2, 34, 54, 55, 1, 0, 76, 21, 1]
numbers2 = [98, 3, 21, 65, 5, 2]

word1 = 'abcdgetfwrsksh'
word2 = 'hgjtyhbdgfshajhjikjj'

words1 = ['John', 'Eve', 'Steve', 'Alex']
words2 = ['Jacob', 'Mark', 'Liv']

common_elements(numbers1, numbers2)
common_elements(word1, word2)
common_elements(words1, words2)
all_elements(numbers1, numbers2)
all_elements(word1, word2)
all_elements(words1, words2)
