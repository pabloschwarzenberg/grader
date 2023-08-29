#Descomponer un número
n=int(input("Ingrese numero",))

d1 = str(n%10)
d2 = str((n%100)//10)
d3 = str((n%1000)//100)
d4 = str((n%10000)//1000)

print(d4+"M","+",d3+"C","+",d2+"D","+",d1+"U")
