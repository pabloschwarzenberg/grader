#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.

#Entrada.

numero = int(input("ingrese el numero de telefono: "))
hora = int(input("ingrese la hora de la llamada: "))

#Operaciones.

if hora >= 0 and hora <= 7:
    print("contestar")
elif numero%1000 == 909:
    print("contestar")
else:
    hora >= 8 and hora <= 16
    print("no contestar")
if numero//100000 == 877:
    print("No contestar")
else:
    hora >= 17 and hora <= 23
    print("contestar")
    