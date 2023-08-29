#Ordenar tres números
n1=int(input("ingrese primer valor: "))
n2=int(input("ingrese segundo valor: "))
n3=int(input("ingrese tercer valor: "))

o1=[n1, n2, n3]
o2=[n1, n3, n2]
o3=[n2, n1, n3]
o4=[n2, n3, n1]
o5=[n3, n1, n2]
o6=[n3, n2, n1]

if n1<=n2 and n2<=n3 and n1<n3:
    print("el orden numerico es: ",o1)
if n1<=n3 and n3<=n2 and n1<n2:
    print("el orden numerico es de: ",o2)
if n2<=n1 and n1<=n3 and n2<n3:
    print("el orden de menor a mayor es: ",o3)
if n2<=n3 and n3<=n1 and n2<n1:
    print("el orden es: ",o4)
if n3<=n1 and n1<=n2 and n3<n2:
    print("el orden es de: ",o5)
if n3<=n2 and n2<=n1 and n3<n1:
    print("el orden de menor a mayor es de: ",o6)