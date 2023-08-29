# por favor escribe aquí tu función
print("Numeros primos")
Numero=int(input("Ingrese Numero:"))
Es_Primo=True
x=2
while x<Numero-1:
    if Numero % x == 0:
        Es_Primo=False
        break
    x+=1
print("Es primo", Es_Primo)