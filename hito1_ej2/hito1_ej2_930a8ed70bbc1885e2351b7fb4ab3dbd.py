#Contestador de celular
      ##Escribe un programa para contestar automáticamente el celular, dependiendo de la hora en que llega la llamada y el número de teléfono. El número telefónico debe ser representado por un número entero (int) de 8 cifras (por ejemplo 78735653), mientras que la hora es representada por un número entero entre 0 y 23. Las reglas que rigen si contestarás o no son las siguientes:
##Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
##Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
##Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
##Después de las 19:00, no contestas el celular.
##El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla.
num = int(input("Numero que esta llamando {8 digitos}: "))
innum = int(input("Ingrese los 3 primeros numeros: "))
tenum = int(input("Ingrese los 3 ultimos numeros: "))
hor = int(input("Hora de llamada {de 0 a 24}: "))
if hor >= 0 and hor <= 7:
  print("CONTESTAR")
elif hor <= 14 and tenum == 909:
  print("CONTESTAR")
elif hor >= 17 and hor <= 19 and innum == 877:
  print("CONTESTAR")
elif hor >= 19:
  print("NO CONTESTAR")
else:
 print("NO CONTESTAR")