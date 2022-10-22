# user input
length = int(input('Wpisz długość boku prostokąta: '))
height = int(input('Wpisz wysokość prostokąta: '))

res = ""
for i in range(height + 1):
    top = ("*---" * length) + "*"
    res += (top + "\n")
    bottom = "|   " * length + "|"
    if i != height:
        res += bottom + "\n"

print(res)
