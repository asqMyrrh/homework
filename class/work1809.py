l = [0,1]
try:
    l[2]
except IndexError as err:
    print('Неверный индекс, Err')
else:
    print('all is okay')
finally:
    print('sure')
TypeError: '1' + 1
IndexError: 