#Conversión de Decimal a Binario
n = int(input("Ingrese su número: "))
d = "k"
e = []
while d != 1:
    a = n%2
    n = n//2
    e.append(str(a))
    if n == 1:
        e.append(str(n))
        d = 1
h = 0
q = ""
i = -1
while h < len(e):
    q += e[i]
    h+=1
    i+=(-1)
print("resultado="+q)      