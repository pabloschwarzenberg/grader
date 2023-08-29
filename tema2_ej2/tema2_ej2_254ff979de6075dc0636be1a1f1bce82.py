# completa el código de la función
def amigos(lista,lista1):
    l=[]
    suma=0
for i in lista:
        for j in range(1,i):
            for k in lista1:
                if i%j==0:
                    suma+=k
                    l.append(i)
                    l.append(k)
return l
 
lista=[220,10,1184,5,6232,12]
lista1=[284,13,1210,7,6368,1]