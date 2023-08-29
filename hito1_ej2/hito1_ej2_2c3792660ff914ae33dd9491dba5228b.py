#Contestador de celular
n=int(input("Ingrese su numero telefonico:"))
ll=int(input("Ingrese la hora de llamada"))

if 0<=ll<=7:
    print("CONTESTAR")
elif 7<ll<=14:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=ll<=19:
    if n//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
