#Conversión de Decimal a Binario
d = int(input("Ingrese un decimal: "))
x = d
k = []
while (d > 0):
    a = int(float(d % 2))
    k.append(a)
    d = (d - a)/2
string = ""
for j in k[::-1]:
    string = string + str(j)
print("resultado=%s" %(string))
