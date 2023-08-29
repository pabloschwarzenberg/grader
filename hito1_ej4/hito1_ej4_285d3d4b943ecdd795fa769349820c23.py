#Conversión de Decimal a Binario
def binario(n):
    b = ""
    while (n//2) !=0:
        b = str(n%2)+b
        n= n//2
    return str(n) + b

n = int(input("ingrese un numero:"))
print ("resultado=",binario(n))
      