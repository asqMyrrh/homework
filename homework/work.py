import random
import string
from random import choice
import string
num=int(input())
def create (num):
    result = ''
    for i in range (num):
        result += choice(string.ascii_letters)
    return result

#print (create(num))

def count_up_and_low(k):
    u = [x for x in create(num) if x.isupper()]
    l = [x for x in create(num) if x.islower()]
    if u<l:
        return (0)
    if l<u:
        return (1)
    if u==l:
        return (-1)
#print(create(num))
#print(count_up_and_low(num))

def create_str(width):
    def create_list_str(width, num):
        list_ = []
        for i in range(num):
            list_.append(create_str(width))
        return list_


s = string.ascii_letters
n = ""
l = [c for c in s]
def cr_str(width):
    l = [random.choice(string.ascii_letters)for i in range(width)]
    s = ""
    for el in l:
        s += el 
    return s 
#print(cr_str(9))

def cr_list_str(width, num):
    l = [cr_str(width) for i in range(num)]
    s =""
    big = 0
    small =0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        s += el 
        s +=''
        for i in el:
            if i.isupper():
                big += 1
            else:
                small +=1
            if big > small:
                statb += 1
                s +='1'
            elif small > big:
                stats += 1
                s += '0'
            else:
                statr += 1
                s += '-1'

            s += ''
        s += '>A' +str(statb/(statb+stats+statr)*100) + '%'
        s += '>a' +str(statb/(statb+stats+statr)*100) + '%'
        s += 'a == A' +str(statb/(statb+stats+statr)*100) + '%'
        return s

print(cr_list_str(8, 8),)

