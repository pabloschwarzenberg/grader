#Aprobación de créditos
Ingreso = int(input("Ingresa tu monto en pesos:"))
Ano_De_Nacimiento = int(input("Ingresa tu año de nacimiento:"))
Numero_De_Hijos = int(input("Ingresa tu numero de hijos:")) 
Anos_En_El_Banco = int(input("Ingresa tus años de pertenencia en el banco:"))
Estado_Civil = str(input("Ingresa si eres Soltero (S) o Casado (C):"))
Campo_O_Ciudad = str(input("Ingresa si vives en el Campo (R) o en la Ciudad (U):"))

Ano_Actual = 2021 
Edad = Ano_Actual - Ano_De_Nacimiento

if Anos_En_El_Banco > 10 and Numero_De_Hijos >= 2:
    print("APROBADO")

elif str(Estado_Civil) == "C" and Numero_De_Hijos > 3 and Edad > 45 and Edad < 55:
    print("APROBADO")
    
elif Ingreso >  2500000 and str(Estado_Civil) == "S" and str(Campo_O_Ciudad) == "U":
    print("APROBADO")
        
elif Ingreso > 3500000 and Anos_En_El_Banco >  5:
    print("APROBADO")
            
elif str(Campo_O_Ciudad) == "R" and str(Estado_Civil) == "C" and Numero_De_Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")