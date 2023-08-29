#Conversión de Decimal a Binario
Numero=int(input("Ingrese un numero para transformarlo a binario: "))
N=Numero
h=0
while 1 <= N:
    B=N%2
    N=N//2
    h+=1

print("resultado=",bin(Numero)[2:h+2])
