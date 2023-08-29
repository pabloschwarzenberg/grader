#calculadora
numero1=int(input("ingrese numero: "))
cantidad=0
suma=0
maximo=0


while numero1!=-1:
    cantidad=cantidad+1
    suma=suma+numero1
    if maximo<numero1:
        maximo=numero1
    
        
   
    numero1=int(input("ingrese numero: "))
print("cantidad=",cantidad)
print("suma=",suma)
if cantidad==0:
    print("maximo=nd")
else:
    print("maximo=",maximo)      