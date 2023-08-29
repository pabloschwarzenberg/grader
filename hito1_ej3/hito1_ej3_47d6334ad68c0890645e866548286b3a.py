#Aprobación de créditos
ENTRY_MONEY = int(input("Ingrese su sueldo en pesos: "))
YEAR_BORN = int(input("Ingrese su año de nacimiento: "))
AGE = 2021 - YEAR_BORN
CHILDS_NUMBER = int(input("Ingrese cantidad de hijos: "))
YEARS_BANK = int(input("Ingrese la cantidad de años que lleva en este banco: "))
MARITAL_STATUS = input("Indique su estado civil (S) soltero / (C) casado: ")
MARITAL_STATUS = MARITAL_STATUS.upper()
LOCATION = input("Indique donde vive (U) urbano / (R) rural: ")
LOCATION = LOCATION.upper()


if YEARS_BANK > 10 and CHILDS_NUMBER >= 2:
    print ("APROBADO")

elif MARITAL_STATUS == "C" and CHILDS_NUMBER > 3 and AGE >= 45 and AGE <= 55 :
    print ("APROBADO")
    print (AGE)

elif ENTRY_MONEY > 2500000 and MARITAL_STATUS == "S" and LOCATION == "U":
    print ("APROBADO")

elif ENTRY_MONEY > 3500000 and YEARS_BANK > 5:
    print ("APROBADO")

elif LOCATION == "R" and MARITAL_STATUS == "C" and CHILDS_NUMBER < 2:
    print ("APROBADO")

else:
    print ("RECHAZADO")  