ingresos = int(input("ingrese el monto: "))
print("\n")
nacimiento = int(input("ingrese su ano de nacimiento: "))
print("\n")
hijos = int(input("ingrese cuantos hijos tienes: "))
print("\n")
pertenencia = int(input("ingrese cuantos anos lleva en el banco: "))
print("\n")
estado_civil = input("ingrese su estado civil S(soltero)/C(casado): ")
print("\n")
vivienda = input("ingrese de donde proviene U(urbano)/R(rural): ")

anos = 2022 - nacimiento

if pertenencia >= 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "c" and hijos > 3 and (anos > 45, anos < 55):
    print("APROBADO")
elif ingresos >= 250000 and estado_civil == "s" and vivienda == "u":
    print("APROBADO")
elif ingresos >= 350000 and pertenencia >= 5:
    print("APROBADO")
elif vivienda == "r" and estado_civil == "c" and hijos <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")   