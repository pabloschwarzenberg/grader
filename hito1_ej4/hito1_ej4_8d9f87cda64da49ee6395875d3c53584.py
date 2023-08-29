#Conversión de Decimal a Binario
def binario(decimal):
    numbinario = ""
    while decimal//2!=0:
        numbinario = str(decimal%2)+numbinario
        decimal = decimal//2
    return str(decimal)+numbinario
num = int(input("ingresa un número:"))
print("resultado="+binario(num))