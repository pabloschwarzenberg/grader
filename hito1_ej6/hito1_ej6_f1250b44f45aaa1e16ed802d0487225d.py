a1 =input("ingresa el primer numero")
a = int(float(a1))

while str(a) != str(a1):
    a1 =input("ingresa un numero entero para el primer numero")
    a=int(float(a1))
    if str(a)==str(a1):
     break
    
b1 =input("ingresa el segundo numero")
b = int(float(b1))


while str(b) != str(b1):
    b1 =input("ingresa un numero entero para el segundo numero")
    b=int(float(b1))
    if str(b)==str(b1):
     break

c1 =input("ingresa el tercer numero")
c = int(float(c1))


while str(c) != str(c1):
    c1 =input("ingresa un numero entero para el tercer numero")
    c=int(float(c1))
    if str(c)==str(c1):
     break

lista =[a,b,c]
lista.sort()
p1=lista[0]
p2=lista[1]
p3=lista[2]
s = ",".join([str(i) for i in lista])
print(s)