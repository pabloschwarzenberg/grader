#Contestador de celular
#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.

#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.

#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.

#Después de las 19:00, no contestas el celular.

numero_telefonico = str(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de llamada: "))

i = hora_llamada

if i >= 0 and i <= 7:
    print("Contestar")

if i <= 14 and i > 7:
    if numero_telefonico[-3:] == "909":
        print("Contestar")
    else:
        print("No contestar")

if i >= 17 and i <= 19:
    if numero_telefonico[0:3] == "877":
        print("No contestar")
    else:
        print("Contestar")

if i > 19:
    print("No contestar")