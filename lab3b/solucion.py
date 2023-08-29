numeros=[]
numero=int(input("ingrese un numero: "))
while numero!=-1:
    numeros.append(numero)
    numero=int(input("ingrese un numero"))
if len(numeros)==0:
    print("cantidad=0")
    print("suma=0")
    print("maximo=ND")
else:
    print("cantidad=",len(numeros))
    print("suma=",sum(numeros))
    print("maximo=",max(numeros))
