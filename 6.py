n = int(input())
def IsSymmetric(a):
    for i in range(1, n-1): # рассматриваем каждую строку/столбец
        for j in range(n-1): # и каждый элемент в ней/нем
            if a[i][j] != a[j][i]: # если элемент не равен элементу с противоположными координатами, то False
                return False

square = [input().split() for i in range(n)] # вводим строки
if IsSymmetric(square):
    print('YES')
else:
    print('NO')