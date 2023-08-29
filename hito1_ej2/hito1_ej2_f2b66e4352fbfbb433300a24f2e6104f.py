#Contestador de celular
hora_dia = int(input("hora a la que llama:"))
numero_telefono = input("numero telefono:")
resultado = ""

if (hora_dia < 7):
    resultado = "CONTESTAR"
elif (hora_dia < 14 and int(numero_telefono[-3:len(numero_telefono)]) == 909):
    resultado = "CONTESTAR"
elif (hora_dia < 17):
    resultado = "NO CONTESTAR"
elif (hora_dia < 19 and not int(numero_telefono[0:3]) == 877):
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"
print(resultado)
