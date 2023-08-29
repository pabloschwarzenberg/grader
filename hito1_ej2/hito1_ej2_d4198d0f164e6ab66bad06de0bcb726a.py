def reqPhoneNumber():
       while True:
        phoneNumber = input("Ingresa el numero de teléfono: ")
        try:
            if len(phoneNumber) == 8:
                return int(phoneNumber)
            else:
                print("Debes ingresar un numero de 8 dígitos. \nInténtalo de unuevo \n")
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

def reqHourNumber():
       while True:
        hourNumber = input("Ingresa la hora de la llamada: ")
        try:
            hourNumber = int(hourNumber)
            if hourNumber >= 0 and hourNumber <= 23 :
                return int(hourNumber)
            else:
                print("Debes ingresar un numero entre 0 y 24. \nInténtalo de unuevo \n")
        except ValueError:
            print("Debes ingresar un número entero entre 0 y 24. \nInténtalo de unuevo \n")

def getLastNumber(number, qtynumber):
    return number % (10**qtynumber)

def getFirstNumber(number, qtynumber):
    return int(number / (10**(int(len(str(number)))-qtynumber)))

phoneNumber = reqPhoneNumber()
hourNumber = reqHourNumber()

if hourNumber >=0 and hourNumber <= 7:
    print("Resultado: CONTESTAR")
elif hourNumber < 14:
    if getLastNumber(phoneNumber,3) == 909:
        print(getLastNumber(phoneNumber,3))
        print("Resultado: CONTESTAR")
    else:
        print(getLastNumber(phoneNumber,3))
        print("Resultado: NO CONTESTAR")
elif hourNumber >=17 and hourNumber <= 19: 
    if getFirstNumber(phoneNumber,3) == 877:
        print(getFirstNumber(phoneNumber,3))
        print("Resultado: NO CONTESTAR")
    else:
        print(getFirstNumber(phoneNumber,3))
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")