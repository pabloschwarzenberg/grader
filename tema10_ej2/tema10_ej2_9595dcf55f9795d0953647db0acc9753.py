#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
    falta = 0
    eliminar = False
    reemplazar = False

    if len(palabra1) > len(palabra2):
        mayor = palabra1
        menor = palabra2
    elif len(palabra2) > len(palabra1):
        mayor = palabra2
        menor = palabra1
    else:
        mayor = palabra1
        menor = palabra2
    palabra2 = menor
    p = list(palabra2)
    posicion = -1
    for i in mayor:
        posicion = posicion + 1
        encontre = str(menor).find(i)
        palabra = menor
        if encontre == -1:
            falta = falta + 1
            cosa = str(mayor).replace(i,"",1)

            if cosa == palabra:
                eliminar = True
            try:
                p.pop(posicion)
                p.append(i)
                pa = "".join(p)
                if pa == mayor:
                    reemplazar = True
            except:
                    pass
        menor = str(menor).replace(i,"",1)
        
    if falta > 1:
            respuesta = print("+1")   
    elif eliminar == True:
            respuesta = print("IB")
    elif reemplazar == True:
            respuesta = print("1S")
    elif palabra1 == palabra2:
            respuesta = print("0D")
    else:
            respuesta = print("Ta malo")
    return respuesta

if __name__=="__main__":
    pass
           