#Aprobación de créditos
year = 2021
ingresos = int(input("Ingreso: "))
born = int(input("Nacimiento: "))
hijes = int(input("Hijes: "))
cliente = int(input("Tiempo de cliente: "))
estado = input("Estado civil: ")
residencia = input("Residencia:" )

if ((cliente > 10 and hijes >= 2)
    or (estado == "C" and hijes > 3 and 45 <= year - born <= 55)
    or (ingresos > 2500000 and estado == "S" and residencia == "U")
    or (ingresos > 3500000 and cliente > 5)
    or (residencia == "R" and estado == "C" and hijes < 2)):
    print("APROBADO")
else:
    print("RECHAZADO")
     