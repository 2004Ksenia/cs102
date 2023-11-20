from random import randint
a = set()
b = set()
c = set()

for i in range(10):
    a.add(randint(0, 15))
    b.add(randint(0, 15))
    c.add(randint(0, 15))
print(a)
print(b)
print(c)
print((a & b) | (b & c))