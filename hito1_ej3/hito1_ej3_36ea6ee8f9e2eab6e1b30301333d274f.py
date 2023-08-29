#Aprobación de créditos
      
print("Atencion automatizada de creditos de consumo")
print("Responda a las siguientes preguntas:")

#PREGUNTAS


INGRESO= str(input("¿De cuanto es tu ingreso? (En pesos)"))

AÑO_NACIMIENTO= str(input("Ingresa tu año de nacimiento:"))

HIJOS= str(input("Ingresa tu numero de hijos:"))

AÑOS_BANCO= str(input("Ingresa el numero de años de pertenencia al banco:"))

E_CIVIL= str(input("Ingresa tu estado civil: (S: Soltero, C: Casado)"))

VIVIENDA= str(input("¿Vives en campo o ciudad? (U: Urbano, R: Rural)"))


#DATOS SOLICITADOS


if (AÑOS_BANCO > str(10)) and (HIJOS >= str(2)):
    print("APROBADO")

if (E_CIVIL == str("C")) and (HIJOS > str(3)):
    print("APROBADO")

if (INGRESO > str(2500000)) and (E_CIVIL == str("S")) and (VIVIENDA == str("U")):
    print("APROBADO")

if (INGRESO > str(3500000)) and (AÑOS_BANCO > str(5)):
    print("APROBADO")

if (VIVIENDA == str("R")) and (E_CIVIL == str("C")) and (HIJOS < str(2)):
    print("APROBADO")

else:
  print("RECHAZADO")