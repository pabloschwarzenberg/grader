 # Contestador de celular
y = int(input("Numero telefonico:"))
x = int(input("Hora de llamada:"))
if 0 <= x <= 7:
    print("CONTESTAR.")
if 7<=x<=14:
    if y%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR.")
if 17<=x<=19:
    if y//100000==877:
        print("NO CONTESTAR.")
    else:
        print("CONTESTAR.")
if x>=19:
    print("NO CONTESTAR.")   