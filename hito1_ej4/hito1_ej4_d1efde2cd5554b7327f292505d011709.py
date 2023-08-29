def binarizar(decimal):
    binario = ""
    while str(decimal//2) != 0:
        binario = str(decimal%2) + binario
        decimal = str(decimal//2)
    return decimal + binario
n= int(input("ingrese numero a convertir a binario: "))
print("resultado=",binarizar(n))
