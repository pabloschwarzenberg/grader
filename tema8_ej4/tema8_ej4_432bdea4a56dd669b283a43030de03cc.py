def string_lista(txt):
    txt = str(txt)
    lista = []
    for i in txt:
        lista.append(i)
    return lista
def rot13(palabra):
    palabra = str(palabra)
    lista1=["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    lista2=["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    e = 0
    for i in palabra:
        palabra = string_lista(palabra)
        if lista1.count(i) == 0:
            a = lista2.index(i)
            # e = 0
            palabra.remove(i)
            palabra.insert(e,lista2[a])
            e += 1
        if lista2.count(2) == 0:
            a = lista1.index(i)
            palabra.remove(i)
            palabra.insert(e,lista1[a])
            e += 1
    palabra = "".join(palabra)
    return palabra
if __name__ == "__main__":
    pal = str(input("Ingrese palabra: "))
    pal = pal.upper()
    print(rot13(pal))
           