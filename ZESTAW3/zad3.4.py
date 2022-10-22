while True:
    data = input('Podaj liczbę float: ')
    if data == 'stop':
        break
    else:
        try:
            print(float(data))
        except ValueError:
            print('Wprowadzono złe dane!')


