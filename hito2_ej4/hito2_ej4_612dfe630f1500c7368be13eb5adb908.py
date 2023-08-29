p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
#si se pide 1,2 y 3 descuento del 20% a toda la compra
#si se pide el 4 y 5 descuento del 15% a toda la compra

print("1: Juego Pokemon X para Nintendo 3DS, USD 33.77")
print("2: Nintendo 3DS XL, USD 203")
print("3: Juego Mario Kart 7 para Nintendo 3DS, USD 27.58")
print("4: PlayStation 4, USD 348.00")
print("5: FIFA 16, PlayStation 4, USD 51.19")


productos=[]
i=0
cantidad_producto=int(input("\n¿Cuantos productos desea comprar?: "))
while i!=cantidad_producto:

    producto=str(input("\tProducto: "))
    cantidad=str(input("\t\t¿Cuántos?:"))
    prducto_cantidad=(f"{producto},{cantidad}")
    i=i+1
    productos.append(prducto_cantidad)
ver=str(input("¿Ver carrito?: "))
if ver=="ver":
    print(productos)