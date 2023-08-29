x=float(input("Ingrese un número decimal: "))
binario= ""
while x // 2 != 0:
    resto=int(x%2)
    x=int(x/2)
    binario=str(resto)+binario
binario=str(1)+binario        
print("resultado=",binario)

