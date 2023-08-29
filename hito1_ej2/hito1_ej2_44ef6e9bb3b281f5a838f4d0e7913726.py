#Contestador de celular
tel = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))

es909 = tel[-3:] == '909'
es877 = tel[:3] == '877'

resultado = "Resultado: "

if hora >= 0 and hora <= 7:
    resultado += "CONTESTAR"
elif hora > 7 and hora <= 14:
    resultado += "CONTESTAR" if es909 else "NO CONTESTAR"
elif hora >= 17 and hora <= 19:
    resultado += "NO CONTESTAR" if es877 else "CONTESTAR"
elif hora > 19 and hora <= 23:
    resultado += "NO CONTESTAR"
else:
    resultado += "NO CONTESTAR"
    
print(resultado)