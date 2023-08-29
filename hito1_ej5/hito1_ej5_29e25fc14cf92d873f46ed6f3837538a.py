#Cálculo del dígito verificador de un rut
RUT = input("Ingrese su RUT sin puntos ni digito verificador: ")
n = 0
x = 0
N = 2
L= []
X=len(RUT)
Y=len(RUT)

for i in range(len(RUT)):
    X-=1
    L.append(RUT[X])
while Y > 0:
    num = int(L[n])*(N)
    x+=num
    N+=1
    n+=1
    Y-=1
    if N > 7:
        N = 2
    
DIV = x // 11
Restable = x - (11*DIV)
DV = 11 - Restable

if DV == 11:
    DV = 0
if DV == 10:
    DV = "K"
print("dv=", DV)