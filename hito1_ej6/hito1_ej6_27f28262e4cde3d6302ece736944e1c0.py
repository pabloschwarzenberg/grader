#Ordenar tres números
n1=eval(input("ingrese un numero"))
n2=eval(input("ingrese un numero"))
n3=eval(input("ingrese un numero"))
MENOR=0
INTERMEDIO=0
MAYOR=0

if n1<=n2 and n1<=n3:
    MENOR=n1
if n2<=n1 and n2<=n3:
    MENOR=n2
if n3<=n1 and n3<=n2:
    MENOR=n3

if n1>=n2 and n1>=n3:
    MAYOR=n1
if n2>=n1 and n2>=n3:
    MAYOR=n2
if n3>=n1 and n3>=n2:
    MAYOR=n3

if (n1>=n2 and n1<=n3) or (n1<=n2 and n1>=n3):
    INTERMEDIO=n1
if (n2>=n1 and n2<=n3) or (n2<=n1 and n2>=n3):
    INTERMEDIO=n2
if (n3>=n2 and n3<=n1) or (n3<=n2 and n3>=n1):
    INTERMEDIO=n3

print(F"{MENOR},{INTERMEDIO},{MAYOR}")
