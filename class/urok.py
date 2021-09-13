n = int(input())
k =[*range(0, n)]
print(k)


def sort_list (elements):
    for i in range (len(elements)):
        for j in range (len(elements)-i -1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements

def create_list(length, minimum, maximum):
    list_=[]
    for i in range(length):
        list_.append(random.randrage(minimum, maximum))
        return list_

def create_list(length,mn,mx):
    return [random.randrange(mn,mx)for i in range/length]