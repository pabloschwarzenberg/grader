#Contestador de celular
numero = int(input("Ingrese un numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

#caso 1
if 0 <= hora <= 7:
    resultado = "CONTESTAR"
elif hora < 14:
    resultado = "NO CONTESTAR" 
elif 17 < hora < 19:
    resultado = "CONTESTAR"
elif 19 < hora:
    resultado = "NO CONTESTAR"
print(resultado)