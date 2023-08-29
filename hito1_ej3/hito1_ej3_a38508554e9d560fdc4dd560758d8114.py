#Aprobación de créditos
ingreso = int(input("Ingrese sus ingreso en esta tabla de ingresos"))
Año_Nacimiento =int(input("Ingrese su año de nacimiento"))
Numero_Hijos= int(input("Ingrese su numero de hijos"))
Años_Banco =  int(input("Ingrese su tiempo en nuestro banco"))
Estado_Civil =input("Ingrese su estado civil")
Vivienda= input("Vive en campo o ciudad")

if (Años_Banco>=10) or (Numero_Hijos>=2):
    print("APROBADO")
elif (Estado_Civil==C) or (Numero_Hijos>=3) or (Año_Nacimiento>1976<1966):
    print("APROBADO")
elif (ingreso>=2500000) or (Estado_Civil==S) or (Vivienda==U):
    print("APROBADO")
elif (ingreso>=3500000) or (Años_Banco>=5):
    print("APROBADO")
elif (Vivienda==R) or (Estado_Civil==C) or (Numero_Hijos):
    print("APROBADO")

else:
    print("RECHAZADO")      