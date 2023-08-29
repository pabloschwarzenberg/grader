#Aprobación de créditos
ingreso = eval(input("ingreso"))
nacimiento = eval(input("año nacimiento"))
hijos = eval(input("Número de hijos"))
pertenencia_banco = eval(input("Años de pertenencia al banco"))
civil = input("C si es casado, S si es soltero")
vivienda = input("U si es urbana, R si es rural")
rural = "R"
urbana = "U"
edad = int (nacimiento)
if pertenencia_banco >=10 and hijos >=2:
  print("Usted cumple con los requisitos y queda APROBADO")
else:
  if ingreso >=2500000 and civil == "S" and vivienda == "U":
    print("Usted cumple con los requisitos y queda APROBADO")
  else:
    if ingreso >=3500000 and pertenencia_banco >=5:
      print("Usted cumple con los requisitos y queda APROBADO")
    else:
      if vivienda =="R" and civil =="C" and hijos <=2:
        print("Usted cumple con los requisitos y queda APROBADO")
      else:
        if civil == "C" and hijos >=3 and edad>=45 and edad<=55:
          print("Usted cumple con los requisitos y queda APROBADO5")
        else:
          print("Estimado,su credito ha sido RECHAZADO")
           