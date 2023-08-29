numero=int(input("Ingrese numero: "))
num_binario=""
while (numero>0):
    if (numero%2==0):
        num_binario=str(0)+num_binario
    else:
        num_binario=str(1)+num_binario
    numero=numero//2
print("resultado=",num_binario)