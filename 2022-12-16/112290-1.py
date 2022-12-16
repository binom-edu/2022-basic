n = int(input())
a = [int(i) for i in input().split()]
x = int(input())

# список позиций, где элемент присутствует
ans = []
for i in range(len(a)):
    if a[i] == x:
        ans.append(i + 1)
if len(ans) > 0:
    print(*ans)
else:
    print(-1)