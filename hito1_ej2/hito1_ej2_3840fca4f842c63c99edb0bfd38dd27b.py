#Contestador de celular
print("<<<<<CONTESTADOR DE CELULAR>>>>>\n")
numCel = int(input("Ingrese numero telefonico de llamada: "))
hora = int(input("Ingrese hora: "))
#Para los últimos tres digitos
#numCel[6:] == numX
numX = numCel*0.001
numZ = int(numX)
numW = numX - numZ
numB = round(numW,3)
numA = numB*1000
#Para los primeros tres digitos
#numCel[:3] = numY
numY = numCel *0.00001

#Condicion 1
if hora >= 0 and hora <7:
    resultado = 'CONTESTAR'
#Condicion 2
elif hora >=7 and hora < 14:
    if numA >= 909 and numA<910:
        resultado = 'CONTESTAR'
    else:
        resultado = 'NO CONTESTAR' 
#Condicion 3
elif hora >= 17 and hora < 19 and numY < 877 and numY >= 878:
    resultado = 'CONTESTAR'
#Condicion 4
else:
    resultado = 'NO CONTESTAR'

print(resultado)