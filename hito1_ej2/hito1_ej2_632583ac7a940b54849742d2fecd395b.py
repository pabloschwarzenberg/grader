# Entrada
n_telefonico = input("Numero telefonico de 8 digitos: ")
hora = int(input("hora de la llamada: "))



# Procedimiento
# Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
# Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
# Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
# Después de las 19:00, no contestas el celular.

# separacion de digitos
termina = int(n_telefonico[5:])
empieza = int(n_telefonico[:3])

# Procedimiento
# Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
if hora < 8:
    print("contestar")

# Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
elif hora < 14:
    if termina == 909:
        print("contestar")
    else:
        print("no contestar")

# Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
elif 17 <= hora <= 19:
    if empieza == 877:
        print("no contestar")
    else:
        print("contestar")

# Después de las 19:00, no contestas el celular.
elif hora > 19:
    print("no contestar")