#Aprobación de créditos
IP = int(input("ingreso en pesos: " ))
AN = int(input("ingrese año de nacimiento: " ))
HI= int(input("ingrese numero de hijos: " ))
AB= int(input("ingrese años pertenencia al banco: " ))
EC= str(input("ingrese estado civil: " ))
UR= str(input("ingrese donde vive: " ))
edad = 2021-AN
if AB>=10 and HI>=2:
    print("APROBADO")
elif EC=="C"  and HI>3 and  45<=edad<=55:
    print("APROBADO")
elif IP>2500000 and EC=="S" and UR=="U":
    print("APROBADO")
elif UR=="R" and EC=="C" and HI<2:
    print("APROBADO")
else:
    print("rechazado")   