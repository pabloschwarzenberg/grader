numero = int(input("Ingresa numero a transformar :"))
binario = ""

while numero != 0:
    binario = binario + str(numero%2)
    numero = numero//2
    
binario_nuevo = ""

for i in range(len(binario)-1,-1,-1):
    binario_nuevo += binario[i]

binario_nuevo = binario[::-1]
print("resultado=",int(binario_nuevo))