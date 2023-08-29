 a=input("ingrese el primer numero: ")
a=int(a)
b=input("ingrese el segundo numero: ")
b=int(b)
c=input("ingrese el tercer numero: ")
c=int(c)
mayor, medio, menor = 0,0,0
if a > b and a > c:
   mayor= a
   if b > c:
       medio, menor =b, c
   else:
       medio, menor = c, b
elif b > a and b > c:
   mayor= b
   if a > c:
       medio, menor =a, c
   else:
       medio, menor = c, a
else:
    mayor= c
    if a > b:
       medio, menor =a, b
    else:
       medio, menor = b, a
print("el orden es", (menor),",",(medio),",", (mayor))