import random

def getRandomArray(n):
    arr = []
    arr = random.sample(range(-n*20,n*20),k=n)
    return arr

def getSortedArray(n):
    counter = n
    lst = []
    while counter > -1:
        lst.append(counter)
        counter-=1
    print(lst)
    return lst

lst = getRandomArray(2000)
print(lst)
getSortedArray(30)
