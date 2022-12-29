def f(a):
    return (sum(a) - min(a) - max(a)) / 3

a = [int(i) for i in input().split()]
print(min(a), max(a))
print(f(a))