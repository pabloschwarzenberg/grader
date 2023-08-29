p1=[1,33.77]
p1n="Pokemon X"
p2=[2,203]
p2n="Nintendo XL"
p3=[2,27.58]
p3n="Mario Kart 7"
p4=[4,348.00]
p4n="PlayStation 4"
p5=[5,51.19]
p5n="FIFA 16"
lista_ver=[]
lista_precio=[]
lista_n=[]
def carrito(productos):

    for x in p1:
        if int(x)==int(p1[0]):
            lista_ver.append(p1n)
            lista_precio.append(p1[1]*cantidad)
            lista_n.append(p1[0])
        if int(x)==int(p2[0]):
            lista_ver.append(p2n)
            lista_precio.append(p2[1]*cantidad)
            lista_n.append(p2[0])
        if int(x)==int(p3[0]):
            lista_ver.append(p3n)
            lista_precio.append(p3[1]*cantidad)
            lista_n.append(p3[0])
        if int(x)==int(p4[0]):
            lista_ver.append(p4n)
            lista_precio.append(p4[1]*cantidad)
            lista_n.append(p4[0])
        if int(x)==int(p5[0]):
            lista_ver.append(p5n)
            lista_precio.append(p5[1]*cantidad)
            lista_n.append(p5[0])
    return ""
def valor_total(lista_precio):
    if 1 in lista_n and 2 in lista_n and 3 in lista_n:
        precio=sum(lista_precio)
        total=precio-(precio*20)/100
    if  4 in lista_n and 5 in lista_n:
        precio=sum(lista_precio)
        total=precio-(precio*15)/100
    else:
        total=sum(lista_precio)
    return round(total,1)
def ver(lista_ver):
    for i in lista_ver:
        print(i,"x",cantidad)
    return ""
def menu():
    print("¿Que desea Hacer?")
    print("1.Agregar producto al carro.")
    print("2.Ver Productos")
    print("3.Checkout")
    return ""
print("Productos")
print("1.Pokemon X")
print("2.Nintendo XL")
print("3.Mario Kart 7")
print("4.PlayStation 4")
print("5.FIFA 16")
while True:
    menu()
    seleccion = str(input("Seleccione agregar,ver o checkout: "))
    if seleccion=="agregar":
        p = str(input("Ingrese el producto y la cantidad en formato (x,y): "))
        x=int(p[0:1])
        cantidad=int(p[2:3])
        carrito(p)
        print("producto(s) agregado(s)")
        salir=str(input("Desea hacer algo mas?(si o no): "))
        if salir=="no":
            break
    elif seleccion=="ver":
        print(ver(lista_ver))
        salir = str(input("Desea hacer algo mas?(si o no): "))
        if salir=="no":
            break
    elif seleccion=="checkout":
        print(valor_total(lista_precio))
      