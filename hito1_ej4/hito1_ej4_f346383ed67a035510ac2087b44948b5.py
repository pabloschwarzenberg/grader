#Conversión de Decimal a Binario
a= int(input('ingrese el numero: '))

nb= []#numero binario
c= 0
 
while (a/2) != 0:
     e= a%2
     a= a/2
     a= int(a)
     nb.append(e)
     
nb.reverse()

for i in range(len(nb)):
    b= nb[i]*(10**(len(nb)-i))
    c= c+b
c= c/10  
c= int(c)
print('resultado=',c)