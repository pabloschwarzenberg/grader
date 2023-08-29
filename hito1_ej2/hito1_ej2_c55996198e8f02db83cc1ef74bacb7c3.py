#Contestador de celular
#Nombre del creador: Daniel Ugarte
numero = str(input("ingrese el numero de telefono(este debe tener 8 digitos): "))
hora = int(input("Ingrese la hora de llamada(representar la hora con numeros del 0 al 23): "))
m = numero[5:9]
n = numero[0:3]
int(m)
int(n)
if (hora >= 0) and (hora <= 19):
    if(hora <= 7):
        print("CONTESTAR")
    elif (hora >= 7) and (hora <= 14):
        if(m == "909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif (hora >= 17) and (hora <= 19):
        if(n == "877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
else:
    print("NO CONTESTAR")