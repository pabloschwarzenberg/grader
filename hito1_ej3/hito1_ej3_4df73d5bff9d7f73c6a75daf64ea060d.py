#DEFINIR VARIABLES



Ingreso = float (input("INGRESE SU SUELDO EN PESOS:"))

AñoDeNacimiento = int (input("INGRESE SU AÑO DE NACIMIENTO:"))

NumeroDeHijos = int (input("INGRESE NUMERO DE HIJOS:"))

AñosConElBanco = int (input("INGRESE NUMERO DE AÑOS QUE ESTA CON NOSOTROS:"))

EstadoCivil = str ( input ("INGRESE ESTADO CIVIL, SOLTERO (S) O CASADO (C):"))

Ubicacion = str ( input ("INGRESE LUGAR URBANO(U) O RURAL (R):"))


#REQUISITOS PARA TENER EL CREDITO



if AñosConElBanco >= 10 and NumeroDeHijos >= 2:
    print("APROBADO")

elif Ingreso >= 2500000 and EstadoCivil == str ("S"):
    print("APROBADO")

elif Ingreso >= 3500000 and AñosConElBanco >= 5:
    print("APROBADO")

elif NumeroDeHijos <= 2 and Ubicacion == str ("R") and EstadoCivil == str ("C"):
    print ("APROBADO")

elif AñosDeNacimiento == 1975 or 1974 or 1973 or 1972 or 1971 or 1970 or 1969 or 1968 or 1967 or 1966 or 1965 and NumeroDeHijos > 3:
    print("APROBADO")

else:
    print("RECHAZADO")
    

                       

                       

      