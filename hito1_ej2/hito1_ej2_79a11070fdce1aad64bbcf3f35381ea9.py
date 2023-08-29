#Contestador de celular
numero=int(input("Ingresar numero: "))
n=((numero//1)%1000)
n_2=((numero//100000)%1000)
Hora=int(input("ingrese hora de la llamada: "))
if Hora>=0 and Hora<=7:
    print("CONTESTAR")    
elif Hora<14 and n==909:
    print("CONTESTAR")
elif Hora>=17 and Hora<=19 and n_2!=877:
    print("CONTESTAR")
elif Hora>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      