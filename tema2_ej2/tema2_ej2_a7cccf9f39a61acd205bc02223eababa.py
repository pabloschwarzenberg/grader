# completa el código de la función
def amigos(a,b):
    lista1=[]
    lista2=[]
    for i in range(1,a):
        if (a%i == 0):               
            lista1.append(i)
         
    for j in range(1,b):
        if b%j == 0:           
            lista2.append(j)
         
    if sum(lista1)==b and sum(lista2)==a:
        return True

    else:
        return False 