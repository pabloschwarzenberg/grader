#Conversión de Decimal a Binario
n= eval(input("Ingrese un numero: "))
l= ""
while n>0:
    if n%2 == 0:
        l= "0" + l
        n=int(n/2)
    else:
        l= "1" + l
        n=int(n/2)
    
print ("resultado=",l)