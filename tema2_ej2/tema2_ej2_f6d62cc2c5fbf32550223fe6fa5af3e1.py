def amigos(a,b):
    lista_1=[]
    lista_2=[]
    suma_1=0
    suma_2=0
    for i in range(1,a):
        if a%i==0:
            lista_1.append(i)
    for i in lista_1:
        suma_1+=i
    for i in range(1,b):
        if b%i==0:
            lista_2.append(i)
    for i in lista_2:
        suma_2+=i
    if suma_1==b and suma_2==a:
         return True
    else:
        return False
    
 
