#Conversión de Decimal a Binario
def decimal_a_binario(n):
     if(n <= 0):
          return "0"
     b=""
     while(n > 0):
       r=int(n % 2)
       k=int(n / 2)
       b=str(r) + b
     return a
n = int(input("ingrese un decimal:"))
b = decimal_a_binario(n)
print("el resultado=",b)