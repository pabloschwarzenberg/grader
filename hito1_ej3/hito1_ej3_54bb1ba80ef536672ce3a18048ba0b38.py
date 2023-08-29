#Aprobación de créditos
IP = float(input("Ingrese su ingreso en pesos : ")) 
AN = int(input("Ingrese su ano de nacimiento : "))
NH = int(input("Ingrese su cantidad de hijos : "))
AP = int(input("Ingrese sus anos de pertenencia en el banco :"))
EC = input("Ingrese su estado civil (Soltero = S y Casado = C) : ")
CC = input("Ingrese si vive en campo o en ciudad (Urbano = U y Rural = R) : ")


if AP > 10 and NH >= 2 :
    print("APROBADO")
elif CC == "C" and NH >= 3 and (AN >= 45 and AN <= 55) :
    print("APROBADO")
elif IP >= 2500000 and EC == "S" and CC == "U" :
    print("APROBADO")
elif IP >= 3500000 and AP > 5 : 
    print("APROBADO")
elif CC == "R" and EC == "C" and NH <= 2 : 
    print("APROBADO")
else :
    print("RECHAZADO")