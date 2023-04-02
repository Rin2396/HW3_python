def can_eat(sth1, sth2): 
    x1 = sth1[0] # присваиваем значения координат
    y1 = sth1[1]
    x2 = sth2[0]
    y2 = sth2[1]
    return abs(x1-x2) + abs(y1-y2) == 3 # т.к. конь ходит на 2 хода по горизонтали и 1 по вертикали (или наоборот), то в сумме будет 3 шага 
result = can_eat((5, 5), (6, 6))
print('result =',result)