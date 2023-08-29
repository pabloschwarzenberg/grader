#Descomponer un número
# Numero 
n = int(input("Ingrese un número entero de hasta cuatro dígitos: "))

# Descomposicion
u = (n%10)
d = (n%100 - n%10)//10
c = (n%1000 - n%100)//100
m = (n%10000 - n%1000)//1000

if 0<n<10000:
    # Salida
    print("Para", n, "debe imprimir:", m,"M +", c,"C +", d,"D +", u,"U")     