a = input().split() #создаем список
s = 0 # счетчик ВСЕХ пар
for i in range(len(a)): # сравниваем одно из чисел списка
    for t in range(len(a)): # со всеми остальными в списке
        if a[i] == a[t] and i != t: # если числа равны, при этом не являются одним и тем же элементом списка,
            s += 1 # то прибавляем к счетчику
print(s // 2) # счетчик считает ВСЕ пары, т.е. каждая из них повторяется по 2 раза