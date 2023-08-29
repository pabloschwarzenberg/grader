#Aprobación de créditos
I = eval(input("ingrese su ingreso en pesos: "))
A = eval(input("ingrese su año de nacimiento: "))
H = eval(input("ingrese su cantidad de hijos: "))
B = eval(input("ingrese sus años de pertenencia en el banco: "))
E = input("ingrese su estado civil con S si es soltero y C si esta casado: ")
S = input("ingrese si vive en el campo con U si vive en el campo y R si vive en la ciudad: ")
A = 2021 - A
if (B) > (10) and (H) >= (2):
  print("APROBADO")
elif (E) == ("C") and (H) > (3) and (A) > (45) and (A) < (55):
  print ("APROBADO")
elif (I) >= (2500000) and (E) == ("S") and (S) == ("R"): 
  print ("APROBADO")
elif (I) >= (350000) and (B) > (5) :
  print ("APROBADO")
elif (S) == ("U") and (E) == ("C") and (H) < (2) :
  print ("APROBADO")
else:
  print("RECHAZADO")