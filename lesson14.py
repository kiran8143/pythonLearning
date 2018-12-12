import sys
a = str(input())
li = []
for i in a:
    li.append(i)
li.sort()
li.reverse()

for i in li:
    print(i,end='')