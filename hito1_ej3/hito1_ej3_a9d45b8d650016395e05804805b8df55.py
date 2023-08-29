#Aprobación de créditos
Ingreso = int(input("Ingrese su Ingreso: "))
Año_nacimiento = int(input("Ingrese su año de nacimiento: "))
Num_hijos = int(input("Ingrese cuantos hijos tiene usted: "))
Años_pertenencia_banco = int(input("Ingrese antiguedad en el banco: "))
Estado_civil = input("Indique su Estadi Civil / Solter@ o Casad@: ")
Residencia = input("Ingrese domicilio: ")

Año_actual = 2020
edad = Año_actual - Año_nacimiento
if (Años_pertenencia_banco > 10 and Num_hijos >= 2) or (Estado_civil =="C" and Num_hijos > 3 and (edad > 45 or edad < 55)) or \
   (Ingreso > 2500000 and Estado_civil =="S" and Residencia =="U") or \
   (Ingreso > 3500000 and Años_pertenencia_banco > 5) or \
   (Residencia =="R" and Estado_civil =="C" and Num_hijos < 2):
   print("APROBADO")