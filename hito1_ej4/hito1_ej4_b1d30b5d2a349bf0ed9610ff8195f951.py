n= int(input("Ingrese un numero: "))
resultado =''
while n > 0 :
    bin = n % 2
    n = n//2
    resultado = str(bin)+resultado


print("resultado=",resultado.strip())