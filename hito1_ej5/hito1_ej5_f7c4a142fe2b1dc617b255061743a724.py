elif Estado_Civil == "C" and (N_de_hijos > 3) and(EDAD >= 45) and (EDAD <= 55):
    print("APROBADO")
elif Ingreso_peso >= 2500000 and Estado_Civil == "S" and Vivienda  == "U":
    print("APROBADO")
elif Ingreso_peso == 3500000 and Años_banco > 5:
    print("APROBADO")
elif Vivienda == "R" and Estado_Civil == "C" and N_de_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")