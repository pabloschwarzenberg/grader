#Algoritmo de Decimal a Binario
numero_decimal = int(input("Ingrese numero decimal : "))
valor = numero_decimal
numero_binario = ''

#Algoritmo de Decimal a Binario
while valor >= 1 :
    resto = valor // 2   

    if valor - (resto * 2) == 0:
        numero_binario = "0" + numero_binario
    else:
        numero_binario = "1" + numero_binario 

    valor = resto

print("resultado="+str(numero_binario))
