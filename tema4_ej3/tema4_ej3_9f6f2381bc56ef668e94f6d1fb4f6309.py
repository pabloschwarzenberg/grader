def jerigonzo(palabra):

    palabra = list(palabra)
    vocales=["a","e","i","o","u"]
    
    
    z = 0
    for vocales[[0][1][2][3][4]] in palabra:
        for vocales[0] in palabra:
            nueva_palabra = "a" + "p" + "a"
            z <= len(palabra)
            nueva_palabra = str(palabra)
            break
        for vocales[1] in palabra:
            nueva_palabra = "e" + "p" + "e"
            z <= len(palabra)
            nueva_palabra = str(palabra)
            break
        for vocales[2] in palabra:
            nueva_palabra = "i" + "p" + "i"
            z <= len(palabra)
            nueva_palabra = str(palabra)
            break
        for vocales[3] in palabra:
            nueva_palabra = "o" + "p" + "o"
            z <= len(palabra)
            nueva_palabra = str(palabra)
            break
        for vocales[4] in palabra:
            nueva_palabra = "u" + "p" + "u"
            z <= len(palabra)
            nueva_palabra = str(palabra)
            break

    return palabra

if __name__ == "__main__":
  palabra = str((input("Ingrese una palabra:", )))
  print(jerigonzo(palabra), "")
