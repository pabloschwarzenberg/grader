#Contestador de celular
# Contestador
# variables

N = input("Ingresar numero de telefono: ")
H = input("Ingresar hora de la llamada: ")
try:
    N = int(N)
    H = int(H)
    if 10000000 <= N <= 99999999:
        N = str(N)
        list(N)
        print("Numero valido.")
        if 0 <= H <= 7 :
            print("Contestar.")
        elif 8 <= H <= 14:
            if N[5:8] == "909":
                print("Contestar.")
            else:
                print("No contestar.")
        elif 17 <= H <= 19:
            if N[0:3] == "877":
                print("No contestar.")
            else:
                print("Contestar.")
        elif 19 < H <= 23:
            print("No contestar.")
        else:
            print("No contestar.")
    else:
        print("Ingrese un numero de 8 digitos.")
except ValueError:
    print("Datos invalidos.")  