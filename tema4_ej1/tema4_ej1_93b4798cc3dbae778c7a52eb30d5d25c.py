import random
lista=["amarilloamarillo","horahora","sopladasoplada"]
palabra=lista[random.randint(0,2)]
cantidad=random.randint(1,(len(palabra)-1))


def ocultar_letras(palabra,cantidad):
    contador=0
    lista_p=[]
    for i in palabra:
        lista_p.append(i)
    while contador<cantidad:
        espacio=random.randint(0,len(palabra)-1)
        if lista_p[espacio]!="_":
            lista_p[espacio]="_"
            contador+=1
        elif lista_p[espacio=="_"]:
            continue
    return lista_p

palabra_oculta_lista=ocultar_letras(palabra,cantidad)
palabra_oculta="".join(str(x) for x in palabra_oculta_lista)

def revisar_letra(palabra,palabra_oculta,letra):   
    contador=0
    lista_po=[]
    for i in palabra_oculta:
        lista_po.append(i)
    if letra in palabra:
        for i in palabra:
            if letra==i:
                lista_po[contador]=letra
            contador+=1
        palabra_oculta="".join(str(x) for x in lista_po)   
        return palabra_oculta
    else:
        return False
    

if __name__ == "__main__":
    while True:
        global palabra_oculta
        global palabra_oculta_lista
        print(palabra_oculta)
        accion=input("""
(1) ingresar una letra
(2) ingresar la palabra
Que quieres hacer:""")
        if accion=="1":
            letra=input("que letra quieres ingresar:")
            if revisar_letra(palabra,palabra_oculta,letra)==False:
                print("La letra no se encuentra en la palabra")
                continue
            else:
                palabra_oculta=revisar_letra(palabra,palabra_oculta,letra)
        if accion =="2":
            palabra_ingresada=input("ingresa la palabra:")
            if palabra_ingresada==palabra:
                print("has ganado")
                break
            else:
                print("esa no es la palabra, has perdido")
                break
