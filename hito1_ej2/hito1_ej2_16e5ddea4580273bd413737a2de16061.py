telefono = int(input("Ingrese su numero telefonico : "))
hora = int(input("Ingrese la hora en la que se llamo : "))

b = (telefono)//10000000
c = (telefono  - b*10000000)//1000000
d = (telefono  - b*10000000 - c*1000000)//100000
e = (telefono  - b*10000000 - c*1000000- d*100000)//10000
f = (telefono  - b*10000000 - c*1000000 - d*100000 - e*10000)//1000
g = (telefono  - b*10000000 - c*1000000 - d*100000 - e*10000 - f*1000)//100
h = (telefono  - b*10000000 - c*1000000 - d*100000 - e*10000 - f*1000 - g*100)//10
i = (telefono  - b*10000000 - c*1000000 - d*100000 - e*10000 - f*1000 - g*100 -h*10)
while telefono>99999999 or telefono<10000000:
    print("Esa telefono  no es valido\nPorfavor reingrese los datos : ")
    telefono = int(input("Telefono ==> "))
    hora = int(input("Hora ==> "))    
while hora>23 or hora<0:
    print("Esa hora es invalida\nPorfavor reingrese los datos : ")
    telefono = int(input("Telefono==> "))
    hora = int(input("Hora ==> "))
if 0<hora<7:
    print("CONTESTAR")
if hora<14 and g==9 and h==0 and i ==9:
    print("CONTESTAR")
if 7<hora<14 and g!=9 and h!=0 and i !=9:
    print("NO CONTESTAR")
if 17<hora<19 and b==8 and c==7 and d==7:
    print("NO CONTESTAR")
else:
    if 17<hora<19:
        print("CONTESTAR")
if 19<hora<=723:
    print("NO CONTESTAR")