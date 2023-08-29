#Aprobación de créditos
pesos = int(input("Inhrese sus ingresos: "))
año = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su número de hijos: "))
banco = int(input("Ingrese los años que ha estado en el banco: "))
civil = input("Ingrese su estado civil, (si es casado: C y soltero: S): ")
vive= input("Ingrese si (vive en urbano: U o si vive en rural: R):  ")
C= civil
S= civil
c= civil
s= civil
U= vive
R= vive
u= vive
r= vive
Años = 2020 - año

if (banco > 10) and (hijos >= 2):
    print("APROBADO")
elif (civil == c) or (civil == C) and (hijos > 3) and (45 <= Años <= 55):
    print("APROBADO")
elif (pesos > 2500000) and (civil == s) or (civil == S) and (vive == u) or (vive == U):
    print("APROBADO")
elif (pesos > 3500000) and (años_en_el_banco > 5):
    print("APROBADO")
elif (vive == r) or (vive == R) and (civil == c) or (civil == C):
    print("APROBADO")
else:
    print("RECHAZADO")