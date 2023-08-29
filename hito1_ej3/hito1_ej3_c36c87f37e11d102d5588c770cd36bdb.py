#Aprobación de créditos
ingreso = eval(input("ingreso"))
nacim = eval(input("año de nacimiento"))
nhijos = eval(input("numero de hijos"))
perbanco = eval(input("años de pertenencia al banco"))
estado = (input("estado civil (""S"" : soltero, ""C"": casado"))
lugar = (input("Si vive en ciudad o campo ( ""U"" : urbano, ""R"" : rural"))

if perbanco > 10 or nhijos >=2:
   print ("APROBADO")
elif estado == "C" and nhijos > 3 and nacim >= 2020 - 45 or nacim <= 2020 - 55:
   print ("APROBADO")
elif ingreso > 2500000 and estado == "S" and lugar == "U":
   print ("APROBADO")
elif ingreso > 3500000 and perbanco > 5:
   print ("APROBADO")
elif lugar == "R" and estado == "C" and nhijos < 2:
   print ("APROBADO")
else:
     print ("RECHAZADO")