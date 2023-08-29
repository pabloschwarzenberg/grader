#Conversor de decimal a binario

numero=float(input(""))
valores = []
while (numero>0):
    m=int((numero%2))
    valores.append(m)
    numero=numero//2

for x in reversed(valores):
    print (x, end="")

