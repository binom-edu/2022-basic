# https://informatics.msk.ru/mod/statements/view.php?id=2741&chapterid=3152#1

a = [int(i) for i in input().split()]
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=' ')