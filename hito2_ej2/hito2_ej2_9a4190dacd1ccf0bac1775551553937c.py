def validar_secuencias(mensaje):
    estado=0
    mensaje=mensaje.lower()
    m=list(mensaje)
    secuencia=("a","a","a","g","t","c","t","g","a","c")
    if (m in secuencia)==True:
        estado="secuencia correcta"
    else:
        estado="secuencia incorrecta"
    return estado
string=input("Ingrese string: ")
respuesta=validar_secuencias(string)
print(respuesta)