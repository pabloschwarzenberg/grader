#Aprobación de créditos
funcionando = True
while funcionando:
    ingreso = int(input("Digite su ingreso (En pesos): "))
    ano_nacimiento = int(input("Ingrese año de nacimiento: "))
    numero_hijos = int(input("Ingrese numero de hijos : "))
    anos_pertenecia = int(input("Ingrese años de pertenencia al banco: "))
    estado_civil = input("Ingrese estado civil ( S: soltero, C: casado): ")
    zona_residencial = input("Ingrese zona residencial (U para urbano) (R para Rural)): ")
    
    if anos_pertenecia >= 10 and numero_hijos >= 2:
        print("APROBADO")
        funcionando = False
    elif estado_civil == "C" and 1978 > ano_nacimiento < 1968:
        print("APROBADO")
        funcionando = False
    elif ingreso < 2500000 and estado_civil == "S" and zona_residencial == "U":
        print("APROBADO")
        funcionando = False
    elif ingreso < 3500000 and anos_pertenecia > 5:
        print("APROBADO")
        funcionando = False
    elif zona_residencial == "R" and estado_civil == "C" and  numero_hijos < 2:
        print("APROBADO")
        funcionando = False
    else:
        print("Rechazado")
        funcionando = False