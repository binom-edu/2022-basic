import random
a = [random.randint(0, 100) for i in range(20)]
print(*a)

a.sort()
print(*a)

a.sort(reverse=True)
print(*a)