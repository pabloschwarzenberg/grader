#ENTRADA
numero = int(input('Ingrese un numero de hasta 4 digitos: '))


#PROCESAMIENTO
if numero >= 0 and numero <= 9 : 
    primer_digito = int(str(numero)[0])
    mensaje = str(primer_digito) + 'U' 
elif numero >= 10 and numero <= 99 : 
    primer_digito = int(str(numero)[0])
    segundo_digito = int(str(numero)[1])
    mensaje = str(primer_digito) + 'D + ' + str(segundo_digito) + 'U'
elif numero >= 100 and numero <= 999 : 
    primer_digito = int(str(numero)[0])
    segundo_digito = int(str(numero)[1])
    tercer_digito = int(str(numero)[2])
    mensaje = str(primer_digito) + 'C + ' + str(segundo_digito) + 'D + ' + str(tercer_digito) + 'U'
elif numero >= 1000 and numero <= 9999 : 
    primer_digito = int(str(numero)[0])
    segundo_digito = int(str(numero)[1])
    tercer_digito = int(str(numero)[2])
    cuarto_digito = int(str(numero)[3])
    mensaje = str(primer_digito) + 'M + ' + str(segundo_digito) + 'C + ' + str(tercer_digito) + 'D + ' + str(cuarto_digito) + 'U'
else:
    mensaje = 'Numero Invalido'


print(mensaje)      