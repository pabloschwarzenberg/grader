#Conversión de Decimal a Binario
def convertirBase(numeroDecimal,base):
    digitos = "0123456789ABCDEF"

    pilaResiduo = Pila()

    while numeroDecimal > 0:
        residuo = numeroDecimal % base
        pilaResiduo.incluir(residuo)
        numeroDecimal = numeroDecimal // base

    nuevaCadena = ""
    while not pilaResiduo.estaVacia():
        nuevaCadena = nuevaCadena + digitos[pilaResiduo.extraer()]

    return nuevaCadena

print(convertirBase(25,2))
print(convertirBase(25,16))