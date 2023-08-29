rut = input("ingrese rut: ")
rutinverso = rut[::-1]
contador = 2
suma = 0
for caracter in rutinverso:
    suma += (int(caracter) * contador)
    contador += 1
    if contador > 7:
        contador = 2
modulo = suma // 11
resta = suma - (11* modulo)
resultado = 11 - resta

if resultado == 11:
    dv = 0
if resultado == 10:
    dv = "k" 
elif resultado != 10 and resultado != 11:
    dv = resultado
    
print("dv =", dv)