#Escribe un programa que decida por ti si contestaras a un numero desconocido en tu celular, dependiendo
#de la hora que llega la llamada y el numero de telefono. El numero telefonico debe ser representado
#por un numero entero (int) de 8 cifras (por ejemplo 78735653), mientras que la hora es representada
#por un numero entero entre 0 y 23. Las reglas que rigen si contestaras o no son las siguientes:
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podrıa ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el numero termina en 909, ya que ası
#termina el numero de alguien que no quieres guardar en el celular, pero te interesa.
#Durante la tarde, solo contestas entre 17:00 y 19:00, exceptuando un numero que comienza por
#877.
#Despues de las 19:00, no contestas ningun numero desconocido.
#El programa debe preguntar al usuario por la hora del dıa y por el numero de celular que llama, e
#imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla. Ve los siguientes ejemplos de c´omo
#deber´ıa correr tu programa.
#Ejemplo 1
#>>> Ingrese numero telefonico: 77389909
#>>> Ingrese hora de la llamada: 13
#>>> Resultado: CONTESTAR
#Ejemplo 2
#>>> Ingrese numero telefonico: 98927674
#>>> Ingrese hora de la llamada: 20
#>>> Resultado: NO CONTESTAR