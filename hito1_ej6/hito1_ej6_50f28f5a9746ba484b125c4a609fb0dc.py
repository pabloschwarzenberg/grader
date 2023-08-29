from os import system
system ("cls")

print("ingrese primer numero entero")
n1=str(input())
print("ingrese segundo numero entero")
n2=str(input())
print("ingrese tercer numero entero")
n3=str(input())

if n2<=n1 and n3<=n1:
    Mayor=n1
    if n2<n3:
        Medio=n3+","
        Menor=n2+","
    else:
        Medio=n2+","
        Menor=n3+","

elif n1<=n2 and n3<=n2:
    Mayor=n2
    if n1<n3:
        Medio=n3+","
        Menor=n1+","
    else:
        Medio=n1+","
        Menor=n3+","

elif n1<=n3 and n2<=n3:
    Mayor=n3
    if n1<n2:
        Medio=n2+","
        Menor=n1+","
    else:
        Medio=n1+","
        Menor=n2+","

print(Menor ,Medio ,Mayor)