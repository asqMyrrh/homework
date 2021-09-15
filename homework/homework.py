s= {'qq': 1, 'q_q': 3, 'QQ': 2}
def sort(s):
    a = sorted(s, key=lambda x:x[1])
    return a
print(sort(s))