#Aprobación de créditos
Ingresos=int(input("Ingrese sus ingresos mensuales porfavor: "))
Año_Nacimiento=int(input("Ingrese su año de nacimiento: "))
Año_actual=2023
Edad=Año_actual-Año_Nacimiento
Hijos=int(input("Ingrese la cantidad de hijos que tiene: "))
if Hijos>=0:
    Años_Pertenecia_Banco=int(input("Ingrese los años que pertenece al banco: "))
    Estado_Civil=input('''Ingrese su estado civil siguiendo las instrucciones 
(Soltero = S) y (Casado = C)
Ingrese su respuesta aqui: ''')
    Lugar_Residencia=input('''Ingrese su lugar de residencia siguiendo las instrucciones
(Ciudad = U) y (Campo = R)
Ingrese su respuesta aqui: ''')
    
    if Años_Pertenecia_Banco>10 and Hijos>=2:
        print("CREDITO DE CONSUMO APROBADO!!!")
    elif Estado_Civil=="C" and Hijos>3 and Edad>=45 or Edad<=55:
        print("CREDITO DE CONSUMO APROBADO!!!")
    elif Ingresos>2500000 and Estado_Civil=="S" and Lugar_Residencia=="U":
        print("CREDITO DE CONSUMO APROBADO!!!")
    elif Ingresos>3500000 and Años_Pertenecia_Banco>5:
        print("CREDITO DE CONSUMO APROBADO!!!")
    elif Lugar_Residencia=="R" and Estado_Civil=="C" and Hijos<2:
        print("CREDITO DE CONSUMO APROBADO!!!")
    else:
        print("CREDITO DE CONSUMO RECHAZADO!!!")
else:
    print("Ingrese un valor valido porfavor.")   