#Contestador de celular
lista = []
telefono = input("Ingrese numero telefonico(8 digitos): ")
lista = list(telefono)
hora = int(input("Ingrese hora de la llamada (0-23): "))

if 0 <= hora <= 7:
    resultado = "CONTESTAR"
elif 8 <= hora <= 13:
    if (int(lista[5])==9) and (int(lista[6])==0) and (int(lista[7])==9):
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"
elif 14 <= hora <= 16:
    resultado = "NO CONTESTAR"
elif 17 <= hora <= 18:
    if (int(lista[0])==8) and (int(lista[1])==7) and (int(lista[2])==7):
        resultado = "NO CONTESTAR"
    else:
        resultado = "CONTESTAR"
elif 19 <= hora <= 23:
    resultado = "NO CONTESTAR"

print("Resultado:",resultado)