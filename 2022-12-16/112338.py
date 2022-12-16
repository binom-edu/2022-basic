s = input()
s1 = ''
cnt = 0
for i in s:
    if i == 'a':
        s1 = s1 + 'b'
        cnt += 1
    elif i == 'A':
        s1 += 'B'
        cnt += 1
    elif i == 'b':
        s1 += 'a'
        cnt += 1
    elif i == 'B':
        s1 += 'A'
        cnt += 1
    else:
        s1 += i
print(s1)
print(cnt)