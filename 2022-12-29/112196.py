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

a, b = map(int, input().split())
if sumOfDivisors(a) == b and sumOfDivisors(b) == a:
    print('YES')
else:
    print('NO')