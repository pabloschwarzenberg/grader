#calculadora
 n1=int(input("ingrese un numero: "))
cantidad=0
suma=0
maximo=0

while n1!=-1:
    print("el numero vale: ",n1)
    
    if maximo<n1:
        maximo=n1    
    else:
        cantidad=cantidad+1
        suma=suma+n1
        n1=int(input("ingrese un numero: "))
print("cantidad=",cantidad)    
print("suma=",suma)
if cantidad==0:
    print("maximo=nd")
else:
    
    print("maximo=",maximo)