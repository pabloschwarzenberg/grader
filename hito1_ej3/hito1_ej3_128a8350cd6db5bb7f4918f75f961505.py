#Aprobación de créditos
ingreso= int(input("ingreso: "))
nacimiento= int(input("año de nacimiento: "))
hijos= int(input("numero de hijos: "))
banco= eval(input("años de pertenecencia al banco: "))
estado= (input("estado civil: "))
vive= (input("vive en campo o ciudad: "))
if banco>10 and hijos>=2:
      print("APROBADO")
elif hijos>3 and 1976>=nacimiento>=1966 and estado==casado:
             print("APROBADO")
elif ingreso>2500000 and estado==soltero and vive==ciudad:
                  print("APROBADO")
elif ingreso>3500000 and banco>5:
                print("APROBADO")
elif hijos<2 and vive=="campo" and estado=="casado":
                          print("APROBADO")
elif nacimiento==1970:
        print("APROBADO")
else: 
     print("RECHAZADO")