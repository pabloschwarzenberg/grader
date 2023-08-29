#Aprobación de créditos
ingresos = eval(input("coloco sus ingresos: "))
Anacimiento = eval(input("año de nacimiento: "))
edad = (2020 - Anacimiento)
Nhijos = eval(input("numero de hijos actuales: "))
Apertenencia = eval(input("ingrese cuantos años lleva con nosotros: "))
S = 1
C = 2
Ecivil = eval(input("su estado civil es Soltero (1) o Casado (2): "))
U = 1
R = 2
Habitat = eval(input("usted vive en un ambito Urbano(1) o uno Rural(2): "))
Rechazado = "RECHAZADO"
Aprobado = "APROBADO"
Credito = Rechazado
if(Apertenencia >= 10 and Nhijos >= 2):
    Credito = Aprobado
if(Ecivil == 2 and Nhijos >= 4 and edad >= 45 and edad <= 55):
    Credito = Aprobado
if(ingresos >= 2500001 and Ecivil == 1 and Habitat == 1):
    Credito = Aprobado
if(ingresos >= 3500001 and Apertenencia >= 6):
    Credito = Aprobado
if(Habitat == 2 and Ecivil == 2 and Nhijos <= 1):
    Credito = Aprobado
print(Credito)