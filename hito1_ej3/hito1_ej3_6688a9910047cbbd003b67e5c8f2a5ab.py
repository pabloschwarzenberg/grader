#Aprobación de créditos
ingreso=int(input("Ingrese sus ingresos: "))
agno=int(input("Ingrese su agno de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
pertenencia=int(input("Ingrese sus agnos en el banco: "))
estadocivil=str(input("Ingrese su estado civil: "))
coc=str(input("¿Vive en campo o en ciudad?: "))

a=int(2017-agno)

if((pertenencia>10)and(hijos>=2)):
   print("APROBADO")
else:
   if((estadocivil=="C")and(hijos>3)and(45<a<55)):
       print("APROBADO")
   else:
       if((ingreso>2500000)and(estadocivil=="S")and(coc=="U")):
            print("APROBADO")
       else:
           if((ingreso>3500000)and(pertenencia>5)):
                print("APROBADO")
           else:
               if((coc=="R")and(estadocivil=="C")and(hijos<2)):
                    print("APROBADO")
               else:
                   print("RECHAZADO") 