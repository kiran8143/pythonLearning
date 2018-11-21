a = []
a = list("hello")
'''
for i in a:
    print(i)
'''
print(len(a))

print(a[:len(a)])

b = (1,2,3)

for i in b:
    print(i)
print(b[:len(b)])

#b[0] = 1

a = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
b = [1, 90, 910, 400, 500, -5]

print(a[2:5])
print(b[0:4])

a.pop()
print(a)
a.extend("a")
print(a)
a.append("b")
print(a)

print(max(b))
b.sort()
print(b[0])
print(sum(b))