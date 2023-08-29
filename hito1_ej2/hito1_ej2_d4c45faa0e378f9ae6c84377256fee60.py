#Contestador de celular
"""Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada y el número de teléfono.
El número telefónico debe ser representado por un número entero (int) de 8 cifras (por ejemplo 78735653), mientras que
la hora es representada por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
Después de las 19:00, no contestas el celular.
El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” 
en pantalla."""
num=0
hora=0
while True:
    num=int(input("Celular (8 digitos): "))
    if len(str(num))==8:
        break
    else:
        print("Número inválido. Intente nuevamente.")
while True:
    hora=int(input("Ingrese la hora actual (0-23): "))
    if hora>=0 and hora<24:
        break
    else:
        print("Hora inválida. Intente nuevamente. ")
        
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<14:
    if str(num)[-3:]=="909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if str(num)[:3]!="877":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")