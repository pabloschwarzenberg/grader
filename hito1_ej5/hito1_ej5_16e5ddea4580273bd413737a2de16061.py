rut = int(input("Ingrese su RUT : "))
y=str(rut)
w=len(y)
k=w
sumatotal=0
digitos = []
suma = []
multiplicacion=2
for i in range (0,w):

    subcadena=y[k-1:k]
    digitos.append(int(subcadena))
    k-=1

for xd in range(0,w):

    suma.append(digitos[xd]*multiplicacion)
    multiplicacion+=1
    if multiplicacion==8:
        multiplicacion=2


for d in range (0,w):
    sumatotal=sumatotal+suma[d]


division = sumatotal%11
dv=11-division

if dv==11:
    dv="0"
if dv==10:
    dv="K"

print("dv =",dv)