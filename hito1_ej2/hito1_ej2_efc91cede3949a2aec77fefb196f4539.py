"""
Contestador Automático
4.- points possible (ungraded)
Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que
llega la llamada y el número de teléfono. El número telefónico debe ser representado por un
número entero (int) de 8 cifras (por ejemplo 78735653), mientras que la hora es representada
por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
•	Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
•	Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
•	Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
•	Después de las 19:00, no contestas el celular.
El programa debe preguntar al usuario por la hora del día y por el número de celular que llama,
e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla. Algunos ejemplos del comportamiento esperado
del programa son:

Ejemplo 1
>>> Ingrese numero telefonico: 77389909
>>> Ingrese hora de la llamada: 13
>>> Resultado: CONTESTAR
Ejemplo 2
>>> Ingrese numero telefonico: 98927674
>>> Ingrese hora de la llamada: 20
>>> Resultado: NO CONTESTAR
Ejemplo 3
>>> Ingrese numero telefonico: 87765545
>>> Ingrese hora de la llamada: 18
>>> Resultado: NO CONTESTAR
"""

numero = int(input("Número del celular: "))
hora = int(input("Hora del día: "))

numero = str(numero)

if hora >= 0 and hora <= 7:
    print("CONTESTAR")

if hora > 7 and hora < 14:
    if numero[-1] == "9" and numero[-2] == "0" and numero[-3] == "9":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if hora >= 17 and hora <= 19:
    if numero[0] == "8" and numero[1] == "7" and numero[2] == "7":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hora > 19 and hora < 23:
    print("NO CONTESTAR")

#El periodo no mencionado de 14:00 a 16:00 lo consideramos por defecto como NO CONTESTAR
if hora >= 14 and hora <= 16:
    print("NO CONTESTAR")