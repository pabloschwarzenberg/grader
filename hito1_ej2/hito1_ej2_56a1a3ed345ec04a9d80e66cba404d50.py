n_telefonico = input("Numero telefonico de 8 digitos: ")
hora = int(input("hora de la llamada: "))
termina = int(n_telefonico[5:])
empieza = int(n_telefonico[:3])
if hora < 8:
    print("contestar")
if hora < 14:
    if termina == 909:
        print("contestar")
    else:
        print("no contestar")
if 17 <= hora <= 19:
    if empieza == 877:
        print("no contestar")
    else:
        print("contestar")
if hora > 19:
    print("no contestar")