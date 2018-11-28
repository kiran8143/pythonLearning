def printHello():
    print("hello world")

printHello()

def passFunc():
    pass

passFunc()

print("passed")

def plusFunc(a,b):
    print(a+b)

plusFunc(1,3)

def resultPlus(a,b):
    return a+b
print(resultPlus(1,4))

def freeArgs(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(freeArgs(1,2,3,4,5,6,7,8,9,10))

#jump to python
def is_odd(arg):
    if arg%2 == 0:
        print("true")
    else:
        print("false")

is_odd(2)
is_odd(3)

def avg(*args):
    sum = 0
    argCount = 0
    for i in args:
        sum += i
        argCount += 1
    return sum/argCount

print(avg(1,5,3))

def fibonacci(arg):

    if arg == 0:
        return 0
    elif arg == 1:
        return 1
    return fibonacci( arg - 2 ) + fibonacci ( arg -1 )
print("--------------")
print(fibonacci(6))

print("--------------")
x = 10
y = 3

def divided(x,y):
    return x//y , x%y

q ,r = divided(x,y)

print("q :{0} , r :{1}" .format(str(q),str(r)))

x = "a b c d e "
x = x.split()
print(len(x))

'''
x = 150
y = 266
z = 111
sum = x * y * z
dictionary = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}

print(str(sum))
for i in str(sum):
    dictionary[str(i)] += 1

for i in range(10):
    print(dictionary[str(i)])

x = raw_input()
x = x.split()
print(int(x[0])+ int(x[1]))
print(int(x[0])- int(x[1]))
print(int(x[0])* int(x[1]))
print(int(x[0])// int(x[1]))
print(int(x[0])% int(x[1]))
'''