p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
l=[p1,p2,p3,p4,p5]
compra_id = []
compra_cantidad = []
def get_name(id):
    for x in l:
        if x[0] == id:
            return x[1]
def get_value(id):
    for x in l:
        if x[0] == id:
            return x[2]
def descuentos(lista_id,lista_cantidad):
    precio_oferta1 = 0
    precio_oferta2 = 0
    if 1 and 2 and 3 in lista_id:
        for x in lista_id:
            if x == 1 or x==2 or x==3:
                precio_oferta1+=get_value(x)*lista_cantidad[lista_id.index(x)]
        precio_oferta1-=(precio_oferta1*20/100)
    else:
        for x in lista_id:
            if x == 1 or x==2 or x==3:
                precio_oferta1+=get_value(x)*lista_cantidad[lista_id.index(x)]
    if 4 and 5 in lista_id:
        for x in lista_id:
            if x==4 or x==5:
                precio_oferta2+=get_value(x)*lista_cantidad[lista_id.index(x)]
        precio_oferta2-=(precio_oferta2*15/100)
    else:
        for x in lista_id:
            if x==4 or x==5:
                precio_oferta2+=get_value(x)*lista_cantidad[lista_id.index(x)]
        precio_oferta2-=(precio_oferta2*15/100)
    return precio_oferta1+precio_oferta2

print("Bienvenido al sistema de compras de amazon")
while True:
    print("ingrese lo que desea, si desea hacer un chekout, escriba \'checkout\' y si no, escriba el id y la cantidad de su producto")
    user_input=input("Ingrese su opcion")
    if user_input=="checkout":
        print("actualmente lleva: ")
        for x in range(len(compra_id)):
            print("producto:",get_name(compra_id[x]), "cantidad:",compra_cantidad[x])
        print("con un total de:",descuentos(compra_id,compra_cantidad))
        continue
    split=user_input.split(",")
    try:
        for x in range(len(split)):
            split[x]=int(split[x])
    except:
        pass
    if split[0] in compra_id:
        remplazo=compra_id.index(split[0])
        compra_cantidad[remplazo]=compra_cantidad[remplazo]+split[1]
    else:
        compra_id.append(split[0])
        compra_cantidad.append(split[1])
    print(split)
    print(compra_id)
    print(compra_cantidad)