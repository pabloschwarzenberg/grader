numTel = eval(input('Ingrese número telefonico: '))

hora = eval(input('Ingrese hora de la llamada: '))

numTel = str(numTel)

positivo = 'Resultado: CONTESTAR'

negativo = 'Resultado: NO CONTESTAR'

if hora >= 19:
    print(negativo)
elif hora >= 0 and hora <= 7:
    print(positivo)
if numTel[5:8] != 909 and hora <= 14 and hora >= 7:
    print(positivo)
elif numTel[5:8] == 909 and hora <= 14 and hora >= 7:
    print(negativo)
if hora >= 17 and hora <= 19 and numTel[5:7] != 877:
    print(negativo)
elif hora >= 17 and hora <=19 and numTel[5:7] == 877:
    print(positivo)