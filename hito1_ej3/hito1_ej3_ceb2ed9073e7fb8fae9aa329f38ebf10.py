#Aprobación de créditos
i = int(input("Ingresos :"))
an = int(input("Año de nacimiento :"))
edad = 2022-an
nh = int(input("Numero de hijos :"))
apb = int(input("Años de pertenencia al banco :"))
ec = input("Estado civil :")
cc = input("Urbano o Rural :")

if apb > 10 and nh >= 2 :
  print("APROBADO")
elif ec == "C" and nh > 3 and edad >= 45 and edad <= 55 :
  print("APROBADO")
elif i > 2500000 and ec == "S" and cc == "U" :
  print("APROBADO") 
elif i > 3500000 and apb > 5 :
  print("APROBADO")
elif cc == "R" and ec == "C" and nh < 2 :
  print("APROBADO")
else :
  print("RECHAZADO")