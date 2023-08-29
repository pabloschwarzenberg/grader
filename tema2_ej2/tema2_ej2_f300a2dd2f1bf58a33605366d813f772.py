# completa el código de la función
def amigos(a,b):
    i=0
    j=0
    listaa=[]
    listab=[]
    listaj=[]
    listam=[]
    sumaa=0
    sumab=0
    while i<a:
        i+=1
        listaa.append(i)
    while j<b:
        j+=1
        listab.append(j)
    for i_ in listaa:
        if a%i_==0 and i_!=a:
            print(i_)
            sumaa=sumaa+i_
        
    print(sumaa)
    for m in listab:
        if b%m==0 and m!=b:
            print(m)
            sumab=sumab+m
       
    print(sumab)
    if sumaa==b and sumab==a:
        return True
    else:
        return False
           