# sorting algorithms

a = [5,3,4,2,1]

def bubleSort(a):
    for i in range(0,len(a)-1,1):
        for j in range(i,-1,-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

print(bubleSort(a))
