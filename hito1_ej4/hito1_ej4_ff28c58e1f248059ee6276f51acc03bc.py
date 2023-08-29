#Conversión de Decimal a Binario
print("tranformar numero decimal a binario")

dec = int(input("Ingresa un número decimal: "))
bi = ""

while dec > 0:
    
    res = int(dec % 2)
    
    dec = int(dec / 2)
   
    bi = str(res) + bi
    
print("resultado=", bi)
