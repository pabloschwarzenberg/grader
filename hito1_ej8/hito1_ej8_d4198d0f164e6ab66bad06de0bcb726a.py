
def reqNumber(reqText):
    while True:
        number = input(reqText)
        try:
            return str(int(number))
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

number = reqNumber("Ingresa un número de 4 cifras: ")
units =['U','D','C','M']
crossList = [a + b for a,b in zip(number[::-1],units[0:len(number)])]
crossList.reverse()
print(" + ".join(crossList))