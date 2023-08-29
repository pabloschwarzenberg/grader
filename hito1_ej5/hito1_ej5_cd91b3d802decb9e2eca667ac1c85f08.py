#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese R.U.T. de 08 dígitos: "))
posiciones = 7
indice = 1
numero = rut
serie = 7
suma = 0
while indice <= 8:
    digito = int(numero//10**posiciones)
    if indice == 1 or indice == 2:
        if indice ==1:
            suma += digito*3 #1 o 3
        else:
            suma += digito*2 #7
    else:
        suma += digito*serie
        serie-=1
    numero = numero-digito*10**posiciones
    posiciones -= 1
    indice += 1
resto=suma%11
verificador = 11-(suma%11)
if verificador == 11:
    verificador = 0
else:
    if verificador == 10:
        verificador = "k"
print ("dv=" + str(verificador))