telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))


if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >= 14 and hora <17 or str(telefono)[5:] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and str(telefono)[0:3] != "877":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")




# Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
# Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
# Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
# Después de las 19:00, no contestas el celular.