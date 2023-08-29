#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora  = int(input("Ingrese hora de la llamada: "))

if 0 <= hora <= 7:
    x = "CONTESTAR"
if 7 < hora <= 14 and numero%1000 == 909:
    x = "CONTESTAR"
if 17 <= hora <= 19:
    if numero//100000 == 877:
        x = "NO CONTESTAR"
    else:
        x = "CONTESTAR"
if 19 < hora <= 23:
    x = "NO CONTESTAR"
if 14 < hora < 17:
    x = "NO CONTESTAR"

print("Resultado:",x)