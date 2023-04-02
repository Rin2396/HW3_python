stroka = input() # создаем список
fFirst = stroka.find('f') # находим индекс первого вхождения
fLast = stroka.rfind('f') # находим индекс последнего вхождения
if fFirst == -1: # если вхождений нет, то ничего не выводим
    print()
elif fFirst == fLast: # если индексы первого и последнего равны, то выводим только один из них
    print(fFirst)
else:
    print(fFirst, fLast) # иначе выводим и первый, и последний