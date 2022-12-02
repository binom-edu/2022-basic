# https://informatics.msk.ru/mod/statements/view.php?id=2741&chapterid=3153#1

a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] % 2 == 0:
        print(a[i], end=' ')