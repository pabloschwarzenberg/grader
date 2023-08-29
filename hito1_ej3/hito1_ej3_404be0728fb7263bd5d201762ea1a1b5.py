#Aprobación de créditos

ingreso = eval(input("Ingrese su sueldo en pesos: $"))
nacimiento = eval(input("Ingrese su año de nacimiento: "))
hijos = eval(input("Numero de hijos: "))
años = eval(input("Años con el banco: "))
estado = str(input("Estado civil('S':Soltero, 'C': Casado): "))
vive = str(input("Si vive en camp o ciudad('U':Urbano, 'R':rural): "))


if años >= 10 and hijos >= 2:
    print("APROBADO")

elif estado == 'C' and hijos > 3 and 1966 <= nacimiento <= 1976:
        print("APROBADO")

elif ingreso > 2500000 and estado == 'S' and vive == 'U':
        print("APROBADO")

elif ingreso > 3500000 and años > 5:
        print("APROBADO")
elif vive == 'R' and estado == 'C' and hijos <= 2:
        print("APROBADO")
else:
     print("RECHAZADO")      