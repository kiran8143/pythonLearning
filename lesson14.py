'''
import sys
a = str(input())
li = []
for i in a:
    li.append(i)
li.sort()
li.reverse()

for i in li:
    print(i,end='')
def selectedSort(li):
    length = len(li)
    for i in range(0, length-1):
        index = i
        for j in range(i+1,length):
            if li[j] < li[index]:
                temp1 = li[j]
                li[j] = li[i]
                li[i] = temp1
        print(li)
    return li

a = [5,99,6,1,2,7]

a = selectedSort(a)
print(a)

userInput = int(input())
i = 0
li = []

while(i < userInput):
    userNumberInput = int(input())
    li.append(userNumberInput)
    i += 1

li = selectedSort(li)
for i in range(len(li)):
    print(li[i])

userInput = int(input())

def hanoi(ring, start,end,hojyo ):
    if ring == 1:
        
        print(str(start) +" " + str(end))
        return
    else:
        hanoi(ring -1 , start,hojyo,end)
        print(str(start) + " "+ str(end))
        hanoi(ring-1, hojyo,end,start)

print(str(pow(2,userInput)-1))
if userInput < 21:
    hanoi(userInput,1,3,2)


userInput = int(input())

userInput = str(input())

li = list(userInput)
sum = 0
for i in range(0,len(li)):
    sum += int(li[i])

print(sum)
'''

userInput = str(input())
count = 0
for i in userInput:
    print(i,end='')
    count +=1
    if count == 10:
        print("")
        count = 0