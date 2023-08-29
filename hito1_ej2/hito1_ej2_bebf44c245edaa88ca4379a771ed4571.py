#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de llamada: "))

if 0<=hora and hora<=14:
    if 0<=hora and hora<=7:
        print("CONTESTAR")
    else:
        if numero%1000==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
elif 17<=hora and hora<=19:
    if numero//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
