from random import choice 

big_letters = [i for i in range(65, 89)]
little_letters = [i for i in range(97, 122)]


def gen_name(big_letters, little_letters, num):
    i = 1 
    while i < num:
        s = ''
        for x in range(0, 3):
            s += chr(choice(big_letters))
            s += chr(choice(little_letters)) * 8

            if x < 4:
                s += ' '
        yield s 
        i += 1 


ranger = gen_name(big_letters, little_letters, 100)
result = [x for x in ranger]
print(result) 