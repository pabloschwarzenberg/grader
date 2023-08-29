#Aprobación de créditos
ingreso = int (input ("Ingreso: "))
ano_de_nacimiento = int (input ("Año de nacimiento: "))
edad = 2017 - ano_de_nacimiento
numero_de_hijos = int (input ("Numero de Hijos: "))
pertenencia = int (input ("Años de pertenencia al Banco: "))
estado_civil = (input ("Estado Civil: "))
forma_de_vida = ( input("Forma de Vida: "))
S = ("soltero")
C = ("casado")
U = ("urbano")
R = ("rural")

if (pertenencia > 10 and numero_de_hijos > 2):
    print("APROBADO")
elif  estado_civil == C and numero_de_hijos >= 3 and (45 < edad and edad < 55) :
    print("APROBADO")
elif (ingreso > 2500000 and estado_civil == "S" and forma_de_vida == "U"):
    print("APROBADO")
elif (ingreso > 3500000 and pertenencia > 5):
    print("APROBADO")
elif (estado_civil == "C" and forma_de_vida == "R" and numero_de_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")



