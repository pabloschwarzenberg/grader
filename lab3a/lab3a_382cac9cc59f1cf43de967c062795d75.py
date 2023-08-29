numeros=[]
numero=int(input("ingrese un numero: "))
while numero!=-1:
    numeros.append(numero)
    numero=int(input("ingrese un numero"))
if len(numeros)==0:
    print("cantidad=0")
    print("promedio=ND")
    print("minimo=ND")
else:
    print("cantidad=",len(numeros))
    print("promedio=",round(sum(numeros)/len(numeros),1))
    print("minimo=",min(numeros))

      