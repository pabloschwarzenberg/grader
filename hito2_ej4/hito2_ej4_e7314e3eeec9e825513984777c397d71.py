p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
a="Juego Pokemon X para Nintendo 3DS, USD 33.77"
b="Nintendo 3DS XL, USD 203"
c="Juego Mario Kart 7 para Nintendo 3DS, USD 27.58"
d=" PlayStation 4, USD 348.00"
e="FIFA 16, PlayStation 4, USD 51.19"
carro=[]

def compra_articulo(p,c):
    precio=0
    if p==a:
        precio=precio+(33.77*c)
    elif p==b:
        precio=precio+(203*c)
    elif p == c:
        precio = precio + (27.58*c)
    elif p == d:
        precio = precio + (348*c)
    elif p == e:
        precio = precio + (51.19* c)
    return precio
opcion=input("Que desea hacer: ")
while opcion=="comprar":
    a1=float(input("¿Que produto desea comprar?: "))
    b2=float(input("¿Cuantas unidades quiere?: "))
    if a1==1:
        carro.append(a)
    elif a1 == 2:
        carro.append(b)
    elif a1==3:
        carro.append(c)
    elif a1==4:
        carro.append(d)
    elif a1==5:
        carro.append(e)
    compra_articulo(a,b)
    opcion = input("Que desea hacer: ")
if opcion=="ver":
    print(carro)
if opcion=="checkout":
    print(carro,precio)