length = int(input('Podaj długość miarki: '))

ruler = ('|....' * (length-1)) + '|'
begin = '0'

for i in range(1, length):
    num = len(str(i))
    begin += ' ' * (5 - num)
    begin += f"{i}"

result = ruler + '\n' + begin
print(result)