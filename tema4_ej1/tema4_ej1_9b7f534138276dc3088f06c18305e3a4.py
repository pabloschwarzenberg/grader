import random
def ocultar_letras(palabra,cantidad):
    palabra=str(palabra)
    L=list(palabra)
    if len(L)<cantidad:
        return False
    c=1
    p=[]
    while c<=cantidad:
        while True:
            n=random.choice(range(len(L)))
            if n in p:
                continue
            else:
                L[n]="_"
                c=c+1
            p.append(n)
            break
    m="".join(L)
    return m

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta=str(palabra_secreta)
    palabra=str(palabra)
    lista_palabra=list(palabra)
    letra=str(letra)
    rango=list(range(len(palabra_secreta)))
    p=[]
    if palabra_secreta.find(letra)!=-1:
        n=-1
        for i in rango:
            n=palabra_secreta.find(letra,n+1)
            if n==-1:
                break
            p.append(n)
        for i in p:
            lista_palabra[i]=letra
        palabra_secreta="".join(lista_palabra)
        return palabra_secreta        
    else:
        return False

def juego_encontrar_palabras():
    lista_palabras_secretas=[conejo,caballo,perro,gato,murciélago,mariposa,tenedor,cenicienta,raton,belleza,hermandad,fraternidad]
    palabra_secreta=random.choice(lista_palabras_secretas)
    palabra_secreta=str(palabra_secreta)
    lista1=list(palabra_secreta)
    cantidad=random.choice(range(len(lista1)-2))#no sé que número poner de resta
    ocultar_letras(palabra_secreta,cantidad)
    print(m)
    intento1=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento1)
    if intento1==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento1)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento2=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento2)
    if intento2==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento2)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento3=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento3)
    if intento3==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento3)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento4=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento4)
    if intento4==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento4)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento5=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento5)
    if intento5==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento5)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento6=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento6)
    if intento6==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento6)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    intento7=str(input("Ingrese letra para completar palabra o adivine la palabra: "))
    lista2=list(intento7)
    if intento7==palabra_secreta:
        return print("¡Ha descubierto la palabra!")
    elif len(lista2)==1:
        revision=revisar_letra(palabra_secreta,m,intento7)
        if revision==palabra_secreta:
            return print("¡Ha descubierto la palabra!")
        elif revision!=False:
            print(revision)
        else:
            print("La letra no se encuentra en la palabra")
    return print("Ha perdido")

if __name__ == "__main__":
    pass
         