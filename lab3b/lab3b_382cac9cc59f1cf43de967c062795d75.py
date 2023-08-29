maximo=-1
cantidad=0
suma=0
numero=int(input("ingrese un numero: "))
while numero!=-1:
    if numero>maximo:
      maximo=numero
    suma=suma+numero
    cantidad=cantidad+1
    numero=int(input("ingrese un numero"))
if cantidad==0:
    print("cantidad=0")
    print("suma=0")
    print("maximo=ND")
else:
    print("cantidad=",cantidad)
    print("suma=",suma)
    print("maximo=",maximo)

      