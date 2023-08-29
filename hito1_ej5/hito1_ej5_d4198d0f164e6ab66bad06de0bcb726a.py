#Cálculo del dígito verificador de un rut
def reqNumber(reqText):
    while True:
        number = input(reqText)
        try:
            return int(number)
        except ValueError:
            print("Debes ingresar un número entero. \nInténtalo de unuevo \n")

def dvCheck(rut):
    crossLists = zip(str(rut).zfill(8), '32765432')
    pairList = [int(a)*int(b) for a,b in crossLists]
    value = 11 - sum(pairList)%11
    return {10: 'K', 11: '0'}.get(value, str(value))

rut = reqNumber("Ingresa tu numero de RUT, sin puntos ni digito verificador: ")
print("dv=",dvCheck(rut))