import string
d = {'qq' : 1, 'qq_2' :'QQ'}
d['Hello'] = 15
def get_value(d , k):
    if k in d.keys():
        return d[k]
    else:
        return -1
def get_value(d , k):
    return d.get(k , -1)
def ascii_upper():
    d ={}
    for i in range(76 , 79 , 86 , 69 , 85):
        d[chr(i)] = i
    return d
def counter_letters(s):
    d = {}
    for ch in string.ascii_lowercase:
        d[ch] = s.count(ch)
    return d


print(counter_letters('qq'))