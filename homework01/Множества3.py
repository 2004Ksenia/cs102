from random import randint
a = set()
b = set()
c = set()
for i in range(10):
    a.add(randint(0, 10))
    b.add(randint(0, 10))
    c.add(randint(0, 10))
print(a)
print(b)
print(c)
print(b | c)