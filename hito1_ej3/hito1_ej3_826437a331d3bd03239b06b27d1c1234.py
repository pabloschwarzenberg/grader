#Aprobación de créditos
ingreso = int(input("Digame sus ingresos(en pesos): "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2023 - nacimiento
hijos = int(input("Digame cuantos hijos tiene: "))
banco = int(input("Cuantos años a pertenecido a este banco: "))
estado_civil = str(input("Digame su estado civil(S : soltero, C : casado): "))
hogar = str(input("Vive en campo(R) o ciudad(U): "))
if banco > 10 and hijos >= 2 or  estado_civil == "C" and hijos > 3 and 45 <= edad <= 55 or ingreso > 2500000 and estado_civil == "S" and hogar == "U" or hogar == "R" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
         