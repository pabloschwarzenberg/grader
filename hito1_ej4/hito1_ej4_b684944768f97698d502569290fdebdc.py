#Conversión de Decimal a Binario
num = int(input("Ingrese un numero decimal: "))

resto = ""
          
while num//2!=0:
    resto=str(num%2)+resto
    num=num//2
    
    binario=str(num)+resto
    
print("resultado=",binario)