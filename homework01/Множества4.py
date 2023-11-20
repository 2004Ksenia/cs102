from random import randint
a = set()
b = set()
c = set()

for i in range(10):
    a.add(randint(0, 20))
    b.add(randint(0, 20))
    c.add(randint(0, 20))
print((a - b) - c)
