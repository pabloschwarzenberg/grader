#Aprobación de créditos
ingreso=int(input())
ano_nacimiento=int(input())
n_hijos=int(input())
antiguedad=int(input())
estado_civil=input()
tipo_comuna=input()
estado_aprobacion = 0
edad=2021-ano_nacimiento
print(edad)
if antiguedad > 10 and n_hijos >=2:
estado_aprobacion = 1
if estado_civil == "C" and n_hijos >=3 and 45 <=edad <=55=
estado_aprobacion = 1
if ingreso > 2500000 and estado_civil == "S" and tipo_comuna == "U":
estado_aprobacion = 1
if ingreso > 3500000 and antiguedad >5:
estado_aprobacion = 1
if tipo_comuna == "R" and estado_civil == "C" and n_hijos <2:
estado_aprobacion = 1
if estado_aprobacion ==0:
print("rechazado")
else:
print("aprovado")
