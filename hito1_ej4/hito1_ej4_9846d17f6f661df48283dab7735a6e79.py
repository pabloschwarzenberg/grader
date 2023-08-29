#Conversión de Decimal a Binario
def binario(numero):
    Binario = " "
    
    while numero // 2 != 0:
        Binario = str(numero%2) + Binario 
        numero = numero // 2
        
    return str(numero) + Binario

x = float(input("ingrese un numero decimal: "))
resultado = binario(int(x))

print("resultado="+ resultado)