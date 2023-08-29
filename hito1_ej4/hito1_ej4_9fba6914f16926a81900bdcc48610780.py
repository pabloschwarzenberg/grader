def decimalabinario(decimal):
    if decimal <=0:
       return "0"
    bin = ""
    while decimal > 0:
            res= int(decimal % 2)
            decimal = int(decimal / 2)
            bin = str(res) + bin
    return bin

decimal = int(input("Ingresa un número decimal: "))
bin = decimalabinario(decimal)

print("resultado =",bin)