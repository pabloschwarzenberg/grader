numeros=[]
numero=0
cantidad=0
suma=0
promedio=0
valor_minimo=1000
x=0
while numero!=-1:
    numero=input("Ingrese número:")
    if numero=='-1' or numero=='':
        break
    numero=float(numero)
    cantidad=cantidad+1
    numeros.append(numero)
    suma=suma+numero
    promedio=suma/cantidad

print("cantidad=",cantidad)
if cantidad>0:
    print("promedio=",round(promedio,1))
    print("minimo=",min(numeros))
else:
    print("promedio=nd")
    print("minimo=nd")