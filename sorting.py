# sorting algorithms

a = [5,3,4,2,1]

# bubble sort
def bubbleSort(a):
    for i in range(0,len(a)-1,1):
        for j in range(i,-1,-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

print(bubbleSort(a))

# insertion sort
def insertionSort(a):
    for i in range(1, len(a), 1):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            j = j-1
    return a

print(insertionSort(a))

import math

b = [3]
temp = math.sin(3)

for i in range(1, 10000, 1):
    if math.sin(i) < temp:
        b.append(i)
        temp = math.sin(i)

print("The index of the decreasing subsequence is:", b)

c = [2]

for i in range(1, 100, 1):
    c.append(2+1/c[-1])

print(c)

d = []
for i in range(0, 99, 1):
    d.append(c[i+1]-c[i])
print(d)
