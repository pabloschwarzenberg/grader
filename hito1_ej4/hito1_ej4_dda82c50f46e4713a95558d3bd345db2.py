numero = eval(input("Ingrese un número:"))
binario = ""
algo = numero
while(numero > 0):
    resto = numero % 2
    numero = numero // 2
    if(resto == 1):
        binario = binario + "1"
    if(resto == 0):
        binario = binario + "0"
if(algo % 2 == 0):
    print("resultado=", eval(binario[::-1]))
else:
    print("resultado=", eval(binario))