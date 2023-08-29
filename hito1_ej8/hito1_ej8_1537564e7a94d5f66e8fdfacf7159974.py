#Descomponer un número
a=int(input("Ingrese número:"))

b=(a//1000)
c=(a//100)
c2=(c%10)
d=(a//10)
d2=(d%10)
e=(a%10)

if a>9999:
    print("No puede ingresar números con más de 4 dígitos, vuelva a intentralo.")

else:
    print(str(b)+"M +",str(c2)+"C +",str(d2)+"D +",str(e)+"U +")      