#Aprobación de créditos
a1=int(input("Ingreso(en pesos): "))
a2=int(input("Año de nacimiento: "))
a3=int(input("Número de hijos: "))
a4=int(input("Años de pertenencia al banco: "))
a5=input("Estado Civil(S:Soltero y C:Casado): ")
a6=input("Es de una zona(U:Urbana o R:Rural): ")
a7=2016-a2
if a4>10 and a3>=2:
    print("APROBADO")
elif a5=="C" and a7<=55 and a7>=45:
    print("APROBADO")
elif a1>2500000 and a5=="S" and a6=="U":
    print("APROBADO")
elif a1>3500000 and a4>5:
    print("APROBADO")
elif a5=="C" and a6=="R" and a3<2:
    print("APROBADO")
else:
    print("RECHAZADO")
