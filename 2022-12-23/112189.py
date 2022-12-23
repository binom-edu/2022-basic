def magic(a, b, c):
    ans = a
    if b < ans:
        ans = b
    if c < ans:
        ans = c
    return ans

a, b, c = map(int, input().split())
print(magic(a, b, c))