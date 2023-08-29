#Aprobación de créditos
I = int(input("Ingrese sus ingresos en pesos:"))
ADN = int(input("Ingrese su año de nacimiento:"))
NH = int(input("Ingrese su número de hijos:"))
APB = int(input("Ingrese su año de pertenencia al banco:"))
ES = str(input("Ingrese su estado civil, soltero (S) o casado (C):"))
CC = str(input("Ingrese si vive en campo (R) o ciudad (U):"))

C = "casado"
S = "soltero"
R = "rural"
U = "urbano"

if CC == "R" and ES == "C" and 2 > NH:
  print("APROBADO")
else:
  if APB > 10 and NH >= 2:
    print("APROBADO")
  else:
      if ES == "C" and NH > 3 and 1961 <= ADN <= 1971:
        print("APROBADO")
      else:
          if I > 2500000 and ES == "S"  and CC == "U":
              print("APROBADO")
          else:
              if I > 3500000 and APB > 5:
                  print("APROBADO")  
              else: 
                  print("RECHAZADO")
                    
                    

