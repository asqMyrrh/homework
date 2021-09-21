l = [0,1]
#s = str(input())
try:
    l['1' + 1]
except TypeError:
    print('Type error occured')


try:
    a = ['a', 'b', 'c']
    print(a[4])
except IndexError:
    print("Исключение IndexError, индекс списка вне диапазона.")
else:
    print("Успех!")

try:
    a = 100000/0
    print (a)
except ZeroDivisionError:
    print('error404!attentionRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRUNRU')
else:
    print('all is okay dont worry')