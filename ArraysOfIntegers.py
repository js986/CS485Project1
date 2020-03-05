import random

def getRandomArray(n):
    arr = []
    arr = random.sample(range(-n*10,n*10),k=n)
    return arr

def getSortedArray(n):
    counter = n
    lst = []
    while counter > 0:
        lst.append(counter)
        counter-=1
    #print(lst)
    return lst

#Test Case
#lst = getRandomArray(2000)
#print(lst)
#getSortedArray(30)
