from random import randint
b = [10, 100, 1000, 100000, 1000000]
def kubiki():
    for j in b:
        a = {}
        for i in range(j):
            num = randint(1, 6) + randint(1, 6) #сумма
            if num not in a:
                a[num] = 1
            else:
                a[num] += 1
        print('статистика для', j)
        for key, value in a.items():
            print(key, (value/(j/100)))
        print(a)
kubiki()
