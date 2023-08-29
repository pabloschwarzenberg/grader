#Ordenar tres números
a=int(input("numero1: "))
b=int(input("numero2: "))
c=int(input("numero3: "))

cambio=0

if a<b:
    cambio=a
    a=b
    b=cambio
if a<c:
    cambio=a
    a=c
    c=cambio
if b<c:
    cambio=b
    b=c
    c=cambio
print(c,",",b,",",a)