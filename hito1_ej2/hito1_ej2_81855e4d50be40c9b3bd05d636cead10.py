#El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla. Algunos ejemplos del comportamiento esperado del programa son:
#Ejemplo 1
#>>> Ingrese numero telefonico: 77389909
#>>> Ingrese hora de la llamada: 13
#>>> Resultado: CONTESTAR
#Ejemplo 2
#>>> Ingrese numero telefonico: 98927674
#>>> Ingrese hora de la llamada: 20
#>>> Resultado: NO CONTESTAR
#Ejemplo 3
#>>> Ingrese numero telefonico: 87765545
#>>> Ingrese hora de la llamada: 18
#>> Resultado: NO CONTESTAR
nm=eval(input('Ingrese numero telefonico; '))
h=eval(input('Ingrese hora de llamada: '))
if h>=0 and h<=7:
  print('CONTESTAR')
elif h<14:
  (int((h[-3])+(h[-2])+(h[-1])))