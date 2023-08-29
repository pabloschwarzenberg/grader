def dec_a_bin(num):
    binario = ""
    while num > 0:
        residuo = num% 2
        binario = str(residuo) + binario
        num = num // 2
    return binario

num_dec = int(input("Ingrese un número decimal: "))
if num_dec >= 0:
    bin_resultante = dec_a_bin(num_dec)
    print("resultado = ", bin_resultante)
else:
    print("El número decimal ingresado no es válido.")