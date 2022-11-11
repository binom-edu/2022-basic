n = int(input())
h = n // 3600
n %= 3600
m = n // 60
s = n % 60

ms = str(m)
ss = str(s)

print(h, ms.rjust(2, '0'), ss.rjust(2, '0'), sep=':')