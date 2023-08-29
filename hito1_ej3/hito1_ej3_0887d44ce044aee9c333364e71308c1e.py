#Aprobación de créditos
I=eval(input("Indique la cantidad de INGRESOS ECONOMICOS: "))
AN=eval(input("Indique su EDAD: "))
NH=eval(input("Indique cantidad de HIJOS: "))
AB=eval(input("Indique la cantidad de AÑOS DE PERTENENCIA AL BANCO: "))
EC=input("Indique su ESTADO CIVIL siendo S(soltero) y C(casado): ")
CP=input("Indique si vive en zona rural(R) o urbano(U): ")

if AB>=10 and NH>=2:
    print("CREDITO APROBADO")
elif EC=='C' and NH>=3 and 45<=AN<=55:
    print("CREDITO APROBADO")
elif I>=2500000 and EC=='S' and CP=='U':
    print("CREDITO APROBADO")
elif I>=3500000 and AB>=5:
    print("CREDITO APROBADO")
elif EC=="C" and CP=="R" and NH<=2:
    print("CREDITO APROBADO")
else:
    print("CREDITO NO APROBADO")
