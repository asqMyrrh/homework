n = int(input())
k = 1
while n >= k + 1:
    if n % k == 0:
        print(k)
        k = (k + 1)
   

