#Contestador de celular
#Hora en la que llega la llamada y el número de teléfono
#número telefónico debe ser representado por un número entero (int) de 8 cifras
# la hora es representada por un número entero entre 0 y 23.
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.
#El programa debe preguntar al usuario por la hora del día y por el número de celular que llama, e imprimir “CONTESTAR” o “NO CONTESTAR” en pantalla.

numero= input("ingrese numero de telefono:")
hora= int(input("ingrese hora de llamada:")) 
if (hora >=19 and hora <=23):
    print(" NO CONTESTAR") #resultado
elif hora >=0 and hora <=7: #emergencia
    print("CONTESTAR")
elif hora <14 and numero[-3: ] =="909":
    print("CONTESTAR")
elif hora <=14:
    print("NO CONTESTAR")
elif hora >=17 and hora <=19 and numero[:3] == "877":
    print("NO CONTESTAR")
elif hora >=17 and hora<=19:
    print("CONTESTAR")
  