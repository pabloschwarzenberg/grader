#Contestador de celular
 EJERCICIO

# Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada
# y el número de teléfono. El número telefónico debe ser representado por un número entero (int) de 8 cifras
# (por ejemplo 78735653), mientras que la hora es representada por un número entero entre 0 y 23.
# Las reglas que rigen si contestarás o no son las siguientes:

# Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
# Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
# Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
# Después de las 19:00, no contestas el celular.
# El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla. Algunos ejemplos del comportamiento esperado del programa son:


# ========================================================================================


# Telefono de ejemplo 77389909

# ENTRADA: _______________________________________________________________
pregunta_numero = input('Ingrese su número de celular: ')
pregunta_horario = int(input('Ingresar sólo hora del día: '))
numero_excepcional = pregunta_numero[5:9]

# PROCESAMIENTO: _________________________________________________________

if pregunta_horario == 0 or pregunta_horario <= 7 and numero_excepcional == '909':
    print('CONTESTANDO: llamada en el rango 00:00 a 07:00 horas')
    print('CONTESTAR')
elif pregunta_horario <= 14 and numero_excepcional == '909':
    print('CONTESTANDO: llamada en el rango 14:00 horas a número excepcional finalizado en 909')
    print('CONTESTAR')
elif pregunta_horario >= 17 and pregunta_horario <= 19 and numero_excepcional == '877':
    print('CONTESTANDO: llamada en el rango 17:00 a 19:00 horas finalizado 877')
    print('CONTESTAR')
else:
    print('NO DISPONIBLE: Me puedes llamar entre 00 a 07 horas. Gracias')
    print('NO CONTESTAR')
# SALIDA: ________________________________________________________________
     