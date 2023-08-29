clp=int(input("Ingrese Credito a solicitar (clp): "))
año=int(input("Ingrese año de nacimiento (dd,mm,año): "))
hijos=int(input("Cuantos hijos tiene: "))
Banco=int(input("Ingrese año de en este banco: "))
Ec=input("Ingrese su estado civil S(soltero)-C(Casado): ")
Localidad=input("Vive en campo u ciudad U(Urbano)-R(Rural): ")

while True:
    if Banco>10:
       if hijos>=2:
         print("\033[4;42m"+"APROBADO")
         break
    if Ec=="C":
      if hijos>3:
         if (año-2020)>=45 and (año-2020)<=55:
           print("\033[4;42m"+"APROBADO")
         break
    if clp>2500000:
       if Ec=="S":
          if Localidad=="U":
             print("\033[4;42m"+"APROBADO")
             break
    if clp>3500000:
        if Banco>5:
           print("\033[4;42m"+"APROBADO")
           break

    if Localidad=="R":
       if Ec=="C":
          if hijos<3:
            print("\033[4;42m"+"APROBADO")
            break
    else:
      print("\033[4;41m"+"Rechazado")