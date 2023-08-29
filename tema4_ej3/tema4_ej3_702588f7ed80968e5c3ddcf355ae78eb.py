def jerigonzo(a):
    lista_vocales=["a","e","i","o","u"]
    lista_palabra=[]
    for i in a:
        if i in lista_vocales:
            if i=="a":
                i="apa"
                lista_palabra.append(i)
            elif i=="e":
                i="epe"
                lista_palabra.append(i)
            elif i=="i":
                i="ipi"
                lista_palabra.append(i)
            elif i=="o":
                i="opo"
                lista_palabra.append(i)
            elif i=="u":
                i="upu"
                lista_palabra.append(i)   
        else:
            lista_palabra.append(i)
    imprime=''.join(lista_palabra)
    return imprime

if __name__ == "__main__":
    a=input("Ingrese palabra:")
    print(jerigonzo(a))