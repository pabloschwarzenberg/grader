#Contestador de celular
numeroOk = False
numero = 0
hora = 0

while numeroOk == False:
    numero = input("Ingrese numero telefonico de 8 cifras")
    if len(numero) == 8:
        numeroOk = True

horario = False
while horario == False:
    hora = input("Ingrese hora ( 0 a 23 )")
    if len(hora) >= 0 and len(hora) <= 23:
        horario = True

numero = int(numero)
hora = int(hora)

if hora >= 0 and hora <= 7:
    print("Resultado: Contestar")
elif hora < 14:
    numeroStr = str(numero)
    ultimosDigitos = int(numeroStr[len(numeroStr)-3:len(numeroStr)])
    if ultimosDigitos == 909:
        print("Resultado: Contestar")
    else:
        print("Resultado: No Contestar")
elif hora >= 17 and hora <= 19:
    primerosNumeros = int(str(numero)[0:3])
    if primerosNumeros != 877:
        print("Resultado: Contestar")
    else:
        print("Resultado: No Contestar")
elif hora > 19:
    print("Resultado: No Contestar")
else:
    print("Resultado: No Contestar")   