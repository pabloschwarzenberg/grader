i = eval(input("¿Cuales son sus ingresos en pesos? "))
a = eval(input("¿En que año nacio? "))
h = eval(input("¿Cuantos hijos o hijas tiene? "))
a2 = eval(input("¿Cuantos años lleva en nuestro banco? "))
ec = str(input("¿Su estado civil es? Representelo con una C si es casado y si es soltero con una S: "))
cc = str(input("¿Su recidencia es en el campo o ciudad? Representelo con una R si es en el campo o con una U si es en la ciudad: "))
age = (2021-a)

if (a2 >= 10) and (h >= 2):
  print("Señor o Señora SU CREDITO A SIDO APROBADO") 
elif (ec == "C") and (h >= 3) and ((age >= 45) or (age <= 55)):
  print("Señor o Señora SU CREDITO A SIDO APROBADO") 
elif (i > 2500000) and (ec == "S") and (cc == "U"):
  print("Señor o Señora SU CREDITO A SIDO APROBADO")
elif (i > 3500000) and (a2 >= 5):
  print("Señor o Señora SU CREDITO A SIDO APROBADO") 
elif (cc == "R") and (ec == "C") and (h < 2):
  print("Señor o Señora SU CREDITO A SIDO APROBADO") 
else:
  print("Señor o Señora SU CREDITO A SIDO DENEGADO") 