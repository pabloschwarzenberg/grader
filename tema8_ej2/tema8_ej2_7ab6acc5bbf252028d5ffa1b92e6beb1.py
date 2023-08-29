def buscarTodas(a,b):
    posicion=""
    i=0
    for caracter in a:

        if caracter==b:
            posicion=posicion+str(i)+" "
        i=i+1
    return posicion

escrito=input("ingrese el string: ")
letra=input("ingrese la letra a buscar: ")
print(buscarTodas(escrito,letra))

           