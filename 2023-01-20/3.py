import random
a = [random.randint(0, 10000) for i in range(20)]
print(*a)

# сортируем список в порядке возрастания последней цифры
def lastDigit(x):
    return x % 10

a.sort(key=lastDigit)
print(*a)

# сортируем список по количеству цифр в числе
a.sort(key=lambda x: len(str(x)))
print(*a)