N=int(input("Ingrese un número decimal: "))
BIN=bin(N)
b=str(BIN)
print("resultado=",b[2::])