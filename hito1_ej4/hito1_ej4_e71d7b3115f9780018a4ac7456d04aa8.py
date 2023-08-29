#Conversión de Decimal a Binario
num = int(input("Ingrese un número: "))
numbin = ""
while num >=1:
    if num%2 ==0:
        numbin =  str(0) + numbin
        
    else:
        numbin = str(1) + numbin 
        
    num =num//2
print("Resultado=", numbin)