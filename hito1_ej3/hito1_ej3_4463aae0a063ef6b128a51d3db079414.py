#Aprobación de créditos
Ing=int(input("¿Cuál es su ingreso? "))
Byr=int(input("¿En qué año nació? "))
Nhij=int(input("¿Cuántos hijos tiene? "))
Yrbnk=int(input("¿Hace cuántos años pertenece a nuestro banco? "))
Cst=input("¿Cuál es su estado civil? Responda \"C\" para casado/a, o \"S\" para soltero/a ")
Cc=input("¿Vive en el campo o en la ciudad? Responda \"R\" si vive en el campo, o \"U\" si vive en la ciudad ")
import datetime as dt
now=dt.datetime.now()
if(((Yrbnk>10)and(Nhij>=2))or((Cst=="C")and(Nhij>3)and(45<=(now.year-Byr)<=55))or((Ing>2500000)and(Cst=="S")and(Cc=="U"))or((Ing>3500000)and(Yrbnk>5))or((Cc=="R")and(Cst=="C")and(Nhij<2))):
  print("APROBADO")
else:
  print("RECHAZADO")