#Contestador de celular
a = int(input("Ingrse numero telefonico: "))
b = int(input("Ingrese hora de la llamada: "))

b = int(b)
if 0 < b < 7 or 17 < b < 19:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
# no supe como realizarlo correctamente, se me habia olvidado preguntarle con anticipacion profe.