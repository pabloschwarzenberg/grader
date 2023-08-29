n1 = int(input("Ingrese un número para convertir de decimal a binario: ")) 
binario = "" 
while n1 > 0:
    a = n1 % 2 
    b1 = 0 
    b1 = b1 + a 
    decim = n1 // 2 
    n1 = decim 
    if b1 == 0: 
        binario = binario + "0"
    else:
        binario = binario + "1"

binario = list(binario)
binario.reverse()
binario = "".join(binario)
print("resultado="+binario)