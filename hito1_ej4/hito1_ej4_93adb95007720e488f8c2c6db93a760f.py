#Conversión de Decimal a Binario
def conversion(dec):
    if dec <= 0:
        return "0"
    bin = ""
    while dec > 0:
        res = int(dec % 2)
        dec = int(dec / 2)
        bin = str(res) + bin
    return bin


dec= int(input("Ingresa un número decimal: "))
bin = conversion(dec)
print("resultado = " + str(bin))      