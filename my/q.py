while True:
    value = input("integor, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue 
    print('Квадрат числа ' + str(number) + ' = ' + str(number*number),)