k = int(input())
ans = 0
i = 1
while i <= k:
    n = i
    n1 = 0
    while n > 0:
        d = n % 10
        n1 = n1 * 10 + d
        n //= 10
    if n1 == i:
        ans += 1
    i += 1
print(ans)