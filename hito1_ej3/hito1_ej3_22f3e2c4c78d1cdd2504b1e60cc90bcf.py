#Aprobación de créditos
sueldo=int(input("Ingrese Sueldo en pesos:$"))
nacimiento=int(input("Ingrese años de nacimiento: "))
cantdehijos=int(input("Ingrese número de hijos: "))
anobanco=int(input("Ingrese cantidad de años que tiene en el banco:"))
estadocivil=input("Ingrese estado civil ´S´ de solteto o ´C´ de casado: ")
vivienda=input("Donde vive? Ingrese ´U´ de Urbano o ´R´ de Rural: ")
estadocivil=estadocivil.lower()
vivienda=vivienda.lower()
edad=2023-nacimiento 
if anobanco>10 and cantdehijos>=2:
    print("CREDITO APROVADO.")
elif estadocivil == "c" and cantdehijos>3 and edad>45 and edad<55:
    print("CREDITO APROVADO.")
elif sueldo>=2500000 and estadocivil == "s" and vivienda == "u":
    print("CREDITO APROVADO.")
elif sueldo>=3500000 and anobanco>=5:
    print("CREDITO APROVADO.")
elif vivienda == "r" and estadocivil == "c" and cantdehijos<=2:
    print("CREDITO APROVADO.")
else:
    print("CREDITO RECHAZADO.")      