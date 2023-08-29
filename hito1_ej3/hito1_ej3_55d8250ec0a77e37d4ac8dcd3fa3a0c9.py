#Aprobación de créditos
pesos = int(input("Inhrese sus ingresos: "))
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_de_hijos = int(input("Ingrese su número de hijos: "))
años_en_el_banco = int(input("Ingrese los años que ha estado en el banco: "))
estado_civil = input("Ingrese su estado civil, (si es casado: C y soltero: S): ")
lugar_donde_vive= input("Ingrese si (vive en urbano: U o si vive en rural: R):  ")
C= estado_civil
S= estado_civil
c= estado_civil
s= estado_civil
U= lugar_donde_vive
R= lugar_donde_vive
u= lugar_donde_vive
r= lugar_donde_vive

cantidad_de_años = 2020 - año_nacimiento

if (años_en_el_banco > 10) and (numero_de_hijos >= 2):
    print("APROBADO")
elif (estado_civil == c) or (estado_civil == C) and (numero_de_hijos > 3) and (45 <= cantidad_de_años <= 55):
    print("APROBADO")
elif (pesos > 2500000) and (estado_civil == s) or (estado_civil == S) and (lugar_donde_vive == u) or (lugar_donde_vive == U):
    print("APROBADO")
elif (pesos > 3500000) and (años_en_el_banco > 5):
    print("APROBADO")
elif (lugar_donde_vive == r) or (lugar_donde_vive == R) and (estado_civil == c) or (estado_civil == C):
    print("APROBADO")
else:
    print("RECHAZADO")