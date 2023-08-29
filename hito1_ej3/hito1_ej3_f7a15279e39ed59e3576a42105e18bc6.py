#Aprobación de créditos
    
ingreso = int(input("Ingrese ingreso (en pesos):"))
anionacimiento = int(input("Ingrese año nacimiento:"))
numerohijos = int(input("Ingrese numero de hijos:"))
aniospertenencia = int(input("Ingrese años de pertenecencia al banco:"))
estadocivil = input("Ingrese estado civil 'S' de soltero y 'C' de casado:")
urbanorural = input("Ingrese 'U' de urbano o 'R' de rural si vive en ciudad o en campo:")

if aniospertenencia > 10 and numerohijos >=2:
  print("APROBADO")
elif estadocivil == 'C' and numerohijos >3 and anionacimiento in range(1961,1973):
    print("APROBADO")
elif ingreso >2500000 and estadocivil == 'S' and urbanorural == 'U':
     print("APROBADO")
elif ingreso >3500000 and aniospertenencia >5:
    print("APROBADO")
elif urbanorural =='R' and estadocivil == 'C' and numerohijos <2:
    print("APROBADO")
  
else:
 print("RECHAZADO")
  