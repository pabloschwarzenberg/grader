#Contestador Automatico

#ENTRADA
telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

#PROCESAMIENTO
ultimos_digitos = int(str(telefono)[-3:])
primeros_digitos = int(str(telefono)[:3])

if hora >= 0 and hora <= 7 :  #Rango 1
   mensaje = 'CONTESTAR'
elif hora > 7 and hora <= 14 and ultimos_digitos == 909: #Rango 2
    mensaje = 'CONTESTAR'
elif hora >= 17 and hora <= 19 and primeros_digitos == 877 :
    mensaje = 'NO CONTESTAR'
elif hora >= 17 and hora <= 19 and primeros_digitos != 877 :
    mensaje = 'CONTESTAR'
else :
   mensaje = 'NO CONTESTAR'



#SALIDA
print('Resultado: ', mensaje)