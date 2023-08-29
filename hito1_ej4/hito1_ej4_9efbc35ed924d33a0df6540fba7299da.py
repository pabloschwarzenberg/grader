#Conversión de Decimal a Binario
#conversor de numero a binario

numero= eval(input("Ingrese un numero decimal"))
binario=""
while numero !=0:
    unoCero=int(numero%2)
    numero=int(numero/2)
    binario= str(unoCero)+ binario
    
print("resultado=",binario)