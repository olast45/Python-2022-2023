def fibonacci(n):
    # 0,1,1,2,3,5,8...
    # a,b,a+b,a+2b,2a+3b
    a = 0
    b = 1

    for i in range(2, n):
        b = a + b
        a = b - a

    number = a + b
    return number


numb = fibonacci(6)
print(numb)
