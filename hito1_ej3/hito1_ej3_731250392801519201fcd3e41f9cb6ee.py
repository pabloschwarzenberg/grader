#Aprobación de créditos
ingreso=int(input("¿cúal es tu ingreso?:"))
nacimiento=int(input("¿qué año naciste?:"))
hijos=int(input("¿cuántos hijos tienes?:"))
pertenencia=int(input("¿hace cuántos años estás en este banco?:"))
estadocivil=input("¿cuál es tu estado civil?:") 
C= estadocivil
S= estadocivil
vive=input("¿dónde vives? (si es en campo escriba R, si es en ciudad escriba U):")
R = vive
U = vive
if pertenencia > 10 and hijos >= 2:
   print("APROBADO")
elif estadocivil == C and hijos > 3 and ((2018 - nacimiento)> 45 or (2018 - nacimiento)< 55):
     print("APROBADO")
elif ingreso >2500000 and estadocivil==S and vive == U:
     print("APROBADO")
elif ingreso > 3500000 and pertenencia <5:
     print("APROBADO")
elif vive== R and estadocivil==C and hijos < 2:
     print("APROBADO")
else:
     print("RECHAZADO")