from random import randint, randrange

def numRand(x,y):
    cout=1
    while cout<=10:
        number=randint(x,y)
        print(number,end=' ')
        cout+=1
    print()
    
def numRand2(x,y):
    cout=1
    result=[]
    while cout<=10:
        number=randint(x,y)
        result.append(number)
        cout+=1
    return result
