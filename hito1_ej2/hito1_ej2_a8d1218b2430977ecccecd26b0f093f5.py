#Contestador de celular
def contestador():
    #verificar la hora
    if 0 <= hora <= 7:
        resultado = "CONTESTAR"
    elif 7 < hora <= 14 and (telefono%1000) == 909:
        resultado = "CONTESTAR"
    elif 17 <= hora <= 19 and (telefono//100000) == 877:
        resultado = "NO CONTESTAR"
    elif 17 <= hora <= 19:
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"

    print(resultado)

#Escribir datos
telefono = int(input("Ingrese número de teléfono: "))
hora = int(input("Ingrese hora de llamada: "))

contestador()
   