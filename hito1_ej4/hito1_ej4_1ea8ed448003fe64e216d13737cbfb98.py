#Conversión de Decimal a Binario
num= int(input("Ingresar numero: "))
result =''
while num > 0 :
    bin = num % 2
    num = num//2
    result = str(bin) + result


print("resultado=",result.strip())   