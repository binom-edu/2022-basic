import random
a = [random.randint(0, 100) for i in range(20)]
print(*a)

# простая сортировка. функция sorted
b = sorted(a)
print(*b)

# простая сортировка. метод sort
a.sort()
print(*a)