n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

notfound = True
for i in range(len(a)):
    if a[i] == x:
        print(i + 1, end=' ')
        notfound = False
if notfound:
    print(-1) 