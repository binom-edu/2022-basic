def sumOfDivisors(n):
    ans = 1
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            ans += i
            j = n // i
            if i != j:
                ans += j
        i += 1
    return ans

ans = []
a, b = map(int, input().split())
lst = [0] * (b + 1)
for i in range(a, b + 1):
    lst[i] = sumOfDivisors(i)
for i in range(a, b):
    for j in range(i + 1, b + 1):
        if lst[i] == j and lst[j] == i:
            ans.append('(' + str(i) + ',' + str(j) + ')')
if len(ans) > 0:
    print(*ans)
else:
    print(0)