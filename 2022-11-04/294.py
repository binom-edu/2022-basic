# Определить максимум из трех чисел
# Неполная форма ветвления
m = int(input())
b = int(input())
c = int(input())
if b > m:
    m = b
if c > m:
    m = c
print(m)