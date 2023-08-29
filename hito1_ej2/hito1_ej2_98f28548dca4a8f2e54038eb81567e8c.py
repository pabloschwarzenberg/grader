#Contestador de celular
num_tel = str(input("Ingrese un número teléfonico: "))
hora = int(input("Ingrese un horario: "))
if hora >= 0 and hora <= 7:
    print("CONTESTAR")

if hora <= 14:
    if num_tel[-3:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if hora > 17 and hora <= 19:
    if num_tel[0:3] =="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hora > 19:
    print("NO CONTESTAR")