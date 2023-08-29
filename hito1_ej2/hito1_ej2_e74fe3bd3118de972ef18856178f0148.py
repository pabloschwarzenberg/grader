llamada = eval(input("Ingrese número: "))
hora = eval(input("Ingrese hora: "))
if 0 <= hora <= 7:
    print("contestar")

if 0 <= hora <= 14:
    if llamada%1000==909:
        print("contestar")
    else:
        print("No contestar")
if 17 <= hora <= 19:
    if llamada%1000==877:
        print("contestar")
    else:
        print("No Contestar")
if hora > 19:
    print("No contestar")