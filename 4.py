n = int(input()) # вводим кол-во дней
a = ['Манная', 'Гречневая', 'Пшенная', 'Овсяная', 'Рисовая'] # каждая каша имеет свой индекс от 0 до 4
for i in range(n):
    print(a[i % 5]) # чтобы вывести кашу с индексом от 0 до 4, надо номер дня раделить на 5 и вывести элемент с индексом равным остатку
    