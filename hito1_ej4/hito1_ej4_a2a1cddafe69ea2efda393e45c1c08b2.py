def binarizar(decimal):
    binario = ""
    while decimal // 2 != 0:
      binario = str(decimal % 2) + binario
      decimal = decimal // 2
    return str(decimal) + binario
    
numero = int(input("Introduce el numero a convertir a binario: "))
print(binarizar(numero))