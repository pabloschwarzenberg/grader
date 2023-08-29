numero=int(input("digite un numero de hasta 4 cifras: "))
contador=int(1)
control=int(10)
while control<=numero:
    contador= contador+1
    control=control*10
if contador==1:
    print(numero,"U")
elif contador==2:
    numero=str(numero)
    decena=numero[0:1]
    unidad=numero[1:2]
    d=int(decena)
    u=int(unidad)
    print(u,"D","+",d,"U")
elif contador==3:
    numero=str(numero)
    centena=numero[0:1]
    decena=numero[1:2]
    unidad=numero[2:3]
    c=int(centena)
    d=int(decena)
    u=int(unidad)
    print(c,"C","+",d,"D","+",u,"U")
else:
    numero=str(numero)
    miles=numero[0:1]
    centena=numero[1:2]
    decena=numero[2:3]
    unidad=numero[3:4]
    m=int(miles)
    c=int(centena)
    d=int(decena)
    u=int(unidad)
    print(m,"M","+",c,"C","+",d,"D","+",u,"U")

