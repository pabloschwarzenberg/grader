#Aprobación de créditos
ingreso = int(input("Ingrese en pesos el ingreso que posee: "))
nacimiento = int(input("Ingrese el año de su nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
abanco = int(input("Ingrese cuantos años lleva utilizando los servicios de este banco: "))
estado = str(input("Ingrese su estado civil, donde S es soltero y C es casado: "))
locacion = str(input("Ingrese su locación, donde U es urbano y R es rural: "))
ano = (2023 - nacimiento)
if abanco > 10 and hijos >= 2:
  print("Felicidades, su credito ha sido APROBADO.")
else:
  if estado == "c" and hijos > 3 and ano >= 45 and 55 >= ano:
    print("Felicidades, su credito ha sido APROBADO.")
  else:
    if ingreso > 2500000 and estado == "s" and locacion == "U":
      print("Felicidades, su credito ha sido APROBADO.")
    else:
      if ingreso > 3500000 and abanco > 5:
        print("Felicidades, su credito ha sido APROBADO.")
      else:
        if locacion == "R" and estado == "C" and 2 > hijos:
          print("Felicidades, su credito ha sido APROBADO.")
        else:
          print("Lo sentimos, su credito ha sido RECHAZAD0.")
    