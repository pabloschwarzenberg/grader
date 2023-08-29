ingresos = int(input("ingrese sus ingresos en pesos: "))
año = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese la cantidad de hijos: "))
antiguedad = int(input("ingrese el tiempo de pertenencia al banco: "))
estado = str(input("igrese su estado civil,(soltero(S) o casado(C)): "))
vive = str(input("ingrese si vive en un lugar urbano(U) o rural(R): "))

if(antiguedad>=10 and hijos>=2):
    print("APROBADO")
elif(estado=="C" and hijos>3 and año>=1965 and año<=1975):
    print("APROBADO")
elif(ingresos>2500000 and estado=="S" and vive=="U"):
    print("APROBADO")
elif(ingresos>3500000 and antiguedad>5):
    print("APROBADO")
elif(vive=="R" and estado=="C" and hijos<2):
    print("APROBADO")

else:
    print("RECHAZADO")
