p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

def Agregar_al_carro(string):
    producto=string[0]
    cantidad=string[2]
    lista_de_compra=[]
    if producto=="1":
        p1[2]=p1[2]*int(cantidad)
        lista_de_compra.append(p1)
    if producto=="2":
        p2[2]=p2[2]*int(cantidad)
        lista_de_compra.append(p2)
    if producto=="3":
        p3[2]=p3[2]*int(cantidad)
        lista_de_compra.append(p3)
    if producto=="4":
        p4[2]=p4[2]*int(cantidad)
        lista_de_compra.append(p4)
    if producto=="5":
        p5[2]=p1[2]*int(cantidad)
        lista_de_compra.append(p5)
    return lista_de_compra



def descuento(lista_de_compra):
    lista_productos=[]
    precio=0
    for i in lista_de_compra: ## Lista son los productos que compré para saber si le puedo hacer un descuento
        lista_productos.append(i[0])

    for a in lista_de_compra:
        precio+=a[2]
        
    if (1 in lista_productos) and (2 in lista_productos) and (3 in lista_productos):
        precio=precio-(precio*0.2)
    if (4 in lista_productos) and (5 in lista_productos):
        precio=precio-(precio*0.15)
    
    return([precio, lista_de_compra])#lista_productos
       

A= [[1,"Pokemon X",33.77],[4,"PlayStation 4",348.00],[5,"FIFA 16",51.19]]
descuento(A)

def carrito(compra):
    lista_de_compra=[]
    producto1=Agregar_al_carro(compra[0])
    producto2=Agregar_al_carro(compra[1])
    producto3=Agregar_al_carro(compra[2])
    lista_de_compra=producto1+producto2+producto3
    lista_de_productos2=descuento(lista_de_compra)

    if compra[3]=="checkout":
        return round(lista_de_productos2[0],1)
    if compra[3]=="ver":
        return lista_de_productos2[1]
        
    #return lista_de_compra
#compra1=input("ingrese su compra: ")
#print(carrito(compra1))



