# completa el código de la función
def amigos(a,b):
    listaa=[]
    listab=[]
    sumaa=0
    sumab=0
    for i in range(1,a):
        if (a%i==0):
            listaa.append(i)
    for x in range(1,b):
        if (b%x==0):
            listab.append(x)
    for i in range(0,len(listaa)):
        sumaa+=listaa[i]
    for x in range(0,len(listab)):
        sumab+=listab[x]
    if sumaa==b and sumab==a:
        return True
    else:
        return False
            
  

