n = int(input())
n1 = 0
while n > 0:
    d = n % 10
    n1 = n1 * 10 + d
    n //= 10
print(n1)