'''Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada y el número de teléfono. El número telefónico debe ser representado por un número entero (int) de 8 cifras (por ejemplo 78735653), mientras que la hora es representada por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
Después de las 19:00, no contestas el celular.
El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla. Algunos ejemplos del comportamiento esperado del programa son:

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
'''

n_telefonico = str(input("Ingrese numero telefonico: "))
while(not (len(n_telefonico) == 8)):
    n_telefonico = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))
resultado = ''
ult_dig = n_telefonico[-3:len(n_telefonico)]
prim_dig = n_telefonico[0:3]
if(hora >= 0 and hora <= 7):
    resultado = "CONTESTAR"
elif(hora > 7 and hora < 14):
    if(ult_dig == '909'):
        resultado = "CONTESTAR"
    else:
        resultado = "NO CONTESTAR"
elif(hora >= 17 and hora <= 19):
    if(prim_dig == "877"):
        resultado = "NO CONTESTAR"
    else:
        resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"
    
    
print("Resultado:", resultado)