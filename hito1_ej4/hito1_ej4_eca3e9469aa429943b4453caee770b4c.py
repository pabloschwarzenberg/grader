#Conversión de Decimal a Binario

def numero_a_tansformar(numero1):
    if numero1 <= 0:
        return "0"
    numero_binario = ""
    while numero1 > 0:
       numero2 = int(numero1 % 2)
       numero1 = int(numero1 / 2)
       numero_binario = str(numero2) + numero_binario
    return numero_binario

numero1 = int(input("Ingresa un número decimal: "))
numero_binario = numero_a_tansformar(numero1)
print("resultado=",numero_binario)
