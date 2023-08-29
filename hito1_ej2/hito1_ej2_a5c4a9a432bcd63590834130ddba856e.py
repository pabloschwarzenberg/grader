import math

numero_telefonico = int(input("ingresar numero telefonico de 8 digitos: "))
hora = int(input("ingresar hora en la que llama(numeros desde el 0 al 23): "))


if len(str(numero_telefonico)) == 8:
    if hora >= 0 and hora <= 7:
        print("contestar")
    elif hora > 7 and hora <= 14:
        if numero_telefonico % 1000 == 909:
            print(numero_telefonico % 1000)
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")

    elif hora > 17 and hora <= 19:
        if numero_telefonico // 100000 == 877:
            print("no contestar")
        else:
            print("contestar")
    if hora >= 19 and hora <= 23:
        print("no contestar") 