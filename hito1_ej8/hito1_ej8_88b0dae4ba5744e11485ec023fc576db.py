#Descomponer un número
numero = input("Numero de 4 cifras: ")

if len(numero) == 1:
    respuesta = numero + "U"
elif len(numero) == 2:
    respuesta = numero[0] + "D" + "+" + numero[1] + "U"
elif len(numero) == 3:
    respuesta = numero[0] + "C" + "+" + numero[1] + "D" + "+" + numero[2] + "U"
elif len(numero) == 4:
    respuesta = numero[0] + "M" + "+" + numero[1] + "C" + "+" + numero[2] + "D" + "+" + numero[3] + "U"

print(respuesta)