Ingreso = int(input("Agrega Ingreso: $" ))
Ano_Na = int(input("Ingrese Año de Nacimiento: "))
Num_Hijos = int(input("Ingrese Número de Hijo(s): "))
Ano_Per = int(input("Ingrese cantidad de años de socio con el Banco: ")) 
Estado_Civil = str(input("Estado Civil, Casado=C, Soltero=S :"))
Zona_Vive = str(input("Zona de Residencia, U= Urbano, R= Rural: "))
Credito_Aprobado = 0
                      
if(Ano_Per>10 and Num_Hijos>=2):
    Credito_Aprobado = 1
if(Estado_Civil=="C" and Ano_Na>=1966 and Ano_Na<=1976):
    Credito_Aprobado = 1
if(Ingreso>=2500000 and Estado_Civil=="S" and Zona_Vive=="U"):
    Credito_Aprobado = 1
if(Ingreso>=3500000 and Ano_Per>5):
    Credito_Aprobado = 1
if(Zona_Vive=="R" and Estado_Civil=="C" and Num_Hijos<2):
    Credito_Aprobado = 1
if(Credito_Aprobado == 1):
    print("APROBADO")
else:
    print("RECHAZADO")