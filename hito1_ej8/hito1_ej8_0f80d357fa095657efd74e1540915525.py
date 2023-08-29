#Descomponer un número
x = input()
x = x[::-1]

#Unidad
unidad = x[0:1]+"U"

#Decena
decena = x[1:2]+"D"
if decena == "D":
    decena = "0D"

#Centena
centena = x[2:3]+"C"
if centena == "C":
    centena = "0C"

#Unidad de Mil
mil = x[3:4]+"M"
if mil == "M":
    mil = "0M"

#filtrado
if mil == "0M":
    if centena == "0C" and decena == "0D":
        print(unidad)
    elif centena == "0C" and decena != "0D":
        print(decena ,"+", unidad)
    else:
        print(centena, "+", decena, "+", unidad)
else:
    print(mil, "+", centena, "+", decena, "+", unidad)     