#tu programa recibirá como parámetro un número que indicará el largo de las combinaciones de números binarios
#que se deben generar
def meterAlfrente(s,lista):
    return [ s + item for item in lista]

def binarios(m):
    if m == 0:
        return []
    if m == 1:
        return ["0","1"]
    else:
        return meterAlfrente("0",binarios(m-1)) + meterAlfrente("1",binarios(m-1))
        
n=int(input("Ingrese un entero \n"))

for string in binarios(n):
    print(string)
