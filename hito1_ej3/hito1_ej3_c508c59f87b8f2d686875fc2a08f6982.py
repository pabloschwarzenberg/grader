ingreso = int(input("Ingreso: "))
ano_nac = int(input ("Año de nacimiento: "))
hijos = int(input ("Número de hijos: "))
ano_ban = int(input ("Años de pertenencia al banco: "))
estado = input ("Estado civil; casado (C) o soltero (S): ")
vive = input ("Vive en campo (R) o ciudad (U): ")
edad = 2017- int(ano_nac)

if ano_ban>10 and hijos>=2:
        print ("APROBADO")
elif estado=="C" and hijos>3 and 45<=edad and edad<=55:
        print ("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U" :
        print ("APROBADO")
elif ingreso>3500000 and ano_ban>5 :
        print ("APROBADO")
elif vive=="R" and estado=="C" and hijos<2: 
        print ("APROBADO")
else:
    print ("RECHAZADO")
