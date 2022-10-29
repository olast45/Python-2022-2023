def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
        # print(i)
    return result


fact = int(input('Wprowadz liczbe ktorej silnie chcesz wyliczyc: '))
res = factorial(fact)
print(res)


