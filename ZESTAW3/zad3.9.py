sequence = [[1], [0], [1, 2, 3], (4, 5, 6), ()]
result = []

for i in sequence:
    result.append(sum(i))

print(result)
