#Aprobación de créditos
#Aprobación de créditos
ingresos= eval(input("ingreso: "))
fc= eval(input(" año nacimiento: "))
hijos= eval(input("n° hijos: "))
anioscliente= eval(input("años cliente banco: "))
estado = input("(S:soltero,C:casado): ")
casa= input("(U:urbano,R:rural): ")

if anioscliente > 10 and hijos >= 2: 
  print("APROBADO")
elif estado == "C" and hijos > 3 and fc >= 1965 and fc <= 1975:
  print("APROBADO")
elif ingresos > 2500000 and estado == "S" and casa == "U": 
  print("APROBADO")
elif ingresos > 3500000 and anioscliente > 5:
  print("APROBADO")
elif casa == "R" and estado == "C" and hijos < 2: 
  print("APROBADO")
else:
  print("REPROBADO")