#Conversión de Decimal a Binario
def reqNumber(reqText):
    while True:
        number = input(reqText)
        try:
            return int(number)
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

number = reqNumber("Ingresa un número: ")
print("resultado="+format(number,"0b"))      