#Aprobación de créditos
var_ingreso=int(input("Ingreso (en pesos):"))
var_anno_nac=int(input("Año de nacimiento:"))
var_hijos=int(input("Número de hijos:"))
var_anno_bco=int(input("Años de pertenencia al banco:"))
var_est=str(input("Est.civil (S: soltero, C, casado):"))
var_vive=str(input("vive campo o cuidad U:urbano,R: rural):"))

var_edad = 2022 - var_anno_nac
var_est = var_est.upper()
var_vive = var_vive.upper()

if var_anno_bco>10 and var_hijos>=2:
      print("APROBADO")
elif var_est=='C' and var_hijos>3 and var_edad >=45 and var_edad <= 55:
      print("APROBADO")
elif var_ingreso>2500000 and var_est=='S' and var_vive=='U':
      print("APROBADO")
elif var_ingreso>3500000 and var_anno_bco>5:
      print("APROBADO")
elif var_vive=='R' and var_est=='C' and var_hijos<2:
      print("APROBADO")
else:
      print("RECHAZADO ")
