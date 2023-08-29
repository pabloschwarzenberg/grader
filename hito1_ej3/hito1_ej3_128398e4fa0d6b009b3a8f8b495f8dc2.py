#Aprobación de créditos
# Entradas

ingresos = int(input("Ingresos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
banco = int(input("Años de pertenencia al banco: "))
estado = input("Estado civil(S: soltero, C: casado): ")
hogar = input("Campo o ciudad(R: campo, U: ciudad): ")

# Edad 
edad = 2022 - nacimiento

# Proceso

if 10 < banco and 2 <= hijos:
    print("APROBADO.")
elif estado == "C" and 3 < hijos and 45 < edad < 55:
    print("APROBADO.")
elif 2500000 < ingresos and estado == "S" and hogar == "U":
    print("APROBADO.")
elif 3500000 < ingresos and 5 < banco:
    print("APROBADO.")
elif hogar == "R" and estado == "C" and hijos < 2:
    print("APROBADO.")
else:
    print("RECHAZADO.")