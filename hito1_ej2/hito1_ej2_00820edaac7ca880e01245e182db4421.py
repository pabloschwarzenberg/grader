#Contestador de celular
#Entrada
hora = input("hora de la llamada: ")
n_telefonico = input("Numero telefonico de 8 digitos: ")

# Procedimiento


x = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
n_telefnico = x and x and x and x and x and x and x and x

if (hora < str(8)):
    print("contestar")
elif hora > str(7) and hora < str(14):
    print("no contestar")
elif hora > str(16) and hora < str(19):
    print("contestar")
elif hora > str(19):
    print("no contestar")      