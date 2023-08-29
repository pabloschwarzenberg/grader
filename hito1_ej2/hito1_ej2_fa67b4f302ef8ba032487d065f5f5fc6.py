numero = int(input("Ingrese el numero telefonico "))
hora = int(input("ingrese la hora de la llamada"))

if 10000000<numero<99999999:
    if 0<hora<=7:
        print("resultado: CONTESTAR")
    elif  8<hora<=14:
        if numero[6::] == 909:
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    elif 15<hora<=16:
        print("Resultado: CONTESTAR")
    elif 17<hora<=19:
        if numero[::3] == 977:
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    elif 19<hora:
        print("Resultado: NO CONTESTAR")

