# функция вычисляет корни квадратного уравнения
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)
        return [x1, x2]
    if d == 0:
        return [-b / (2 * a)]
    return ['Корней нет']

a, b, c = map(int, input('Введите коэффициенты квадратного уравнения: ').split())
print(*solve(a, b, c))