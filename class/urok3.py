a = list(input())
def unique(a):
    return list(set(a))
print (unique(a))


e = list(input())
g = list(input())
def unique(e, g):
    e = set(e)
    g = set(g)
    c = e.intersection(g)
    return list(c)
print(unique(e, g))