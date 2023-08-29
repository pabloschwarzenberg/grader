#calculadora
cantidad=0
suma=0
minimo=10000
while True:
    l=float(input("ingrese una cantidad de numeros:"))
    if l==-1:
        break
    cantidad=cantidad+1
    suma=suma+l
print("cantidad=",cantidad)
if cantidad>0:
    print("promedio=",round(suma/cantidad,1))
else:
    print("promedio=nd")


    