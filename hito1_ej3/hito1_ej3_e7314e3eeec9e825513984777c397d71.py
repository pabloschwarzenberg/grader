ingreso= float(input("Ingrese su ingreso: "))
año= float(input("Ingrese su año de nacimiento: "))
hijos=float(input("Ingrese la cantidad de hijos: "))
aperte=float(input("Ingrese sus años en el banco: "))
estado=input("Ingrese su estado civil: ")
vive=input("Ingrese el lugar donde vive: ")

if aperte>=10 and hijos>=2:
        print("APROBADO")
else:
     if estado=="C" and 1969<año<1983:
             print("APROBADO")
     else:
          if ingreso>2500000 and estado=="S" and vive=="U":
                  print("APROBADO")
          else:
             if ingreso>3500000 and aperte>5:
                     print("APROBADO")
             else:
               if vive=="R" and estado=="C" and hijos<2:
                  print("APROBADO")
               else:
                  print("RECHAZADO")