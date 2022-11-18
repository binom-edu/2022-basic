# Посчитать количество трехзначных чисел, которые заканчиваются на 3

finger = 0
for i in range(100, 1000):
    if i % 10 == 3:
        finger += 1

print(finger)

# то же самое, но короче
finger = 0
for i in range(103, 1000, 10):
    finger += 1
print(finger)