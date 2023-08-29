#Aprobación de créditos
from datetime import date

def reqNumber(reqText):
    while True:
        number = input(reqText)
        try:
            return int(number)
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

def reqCharResp(charList,reqText):
    while True:
        resp = input(reqText).upper()
        if resp in charList:
            return resp
        else:
            print("Ingresaste un caracter incorrecto \nInténtalo de nuevo \n")

salary = reqNumber("Indica tu ingreso mensual: ")
yearsbirthDate = reqNumber("Indica tu año de nacimiento: ")
children = reqNumber("Indica la cantidad de hijos: ")
yearsInBank = reqNumber("Indica los años en el banco: ")
civilStatus = reqCharResp(["S","C"],"Ingresa tu estado civil ('S' => Soltero , 'C' => Casado): ")
fieldOrCity = reqCharResp(["U","R"],"Ingresa tu lugar de residencia ('U' => Urbano , 'R' => Rural): ")

age = date.today().year - yearsbirthDate

req1 = yearsInBank > 10 and children >= 2
req2 = civilStatus == "C" and children > 3 and  age > 45 and age < 55
req3 = salary > 2500000 and civilStatus == "S" and fieldOrCity == "U"
req4 = salary > 3500000 and yearsInBank > 5
req5 = fieldOrCity == "R" and civilStatus == "C" and children < 2

result = "APROBADO" if req1 or req2 or req3 or req4 or req5 else "RECHAZADO"
print(result)