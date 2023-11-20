from random import randint
a = set()
b = set()
while len(a) < 7:
    a.add(randint(0, 10))
while len(b) < 7:
    b.add(randint(-10, 10))

print(a)
print(b)
if a == b:
    print('Множества совпадают')
if a <= b:
    print('Множество а является подгруппой множества b')
if b <= a:
    print('Множество b является подгруппой множества a')
else:
    print('Пересечение >', a & b)
    print('Объединение >', a | b)
    print('Разность >', a - b)
