#tuple

b = (1,2,3)

for i in b:
    print(i)
print("--------------------")
print(b[:len(b)])

#dic
x = {'a':10 , 'b':3 , 'c' :3}

print(x)
print(x['a'])

x['d'] = 10

print(x)

x['d'] = -1

print(x['d'])

print(len(x))

x.update(a = 100 , b = 200)

print(x)

x['z'] = 111

print(x)
print(x.pop('z'))
print("---------------")
print(x)
print(x.popitem())

print("---------------")
print(x)
print(x.items())
#print(x.values())
xValue = list(x.values())
print(xValue)
x.setdefault("xx",222)
print(x)