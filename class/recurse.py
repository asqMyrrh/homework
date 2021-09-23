#n = 10000
#def f(n):
#    print(n)
 #   if n > 0:
  #      f(n - 1)
#print(f(n))


m = int(input())
n = int(input())
def f(n, m):
    print (n, m)
    if n > m:
        f(n - 7, m)
print(f(n, m))


a = int(input())
def recur_factorial(n):
      if n == 1:
              return n
      else:
              return n*recur_factorial(n - 1)
num = a
if num < 0:
      print('число то ОТРИЦАТЕЛЬНОЕ, так не пойдет')
elif num == 0:
      print("Факториал 0 это 1")
else:
      print("Факториал",num,"равен",recur_factorial(num))


def dividers(n, div = 1, all_divs = []):
    if n == div:
        all_divs.appond(div)
        return all_divs
    elif div < n:
        if n % div == 0:
            all_divs.append(div)
        return dividers(n, div = div + 1, all_divs = all_divs)
    else:
        print("ты не прав с n", n)
