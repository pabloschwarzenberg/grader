#Ordenar tres números
a=int(input("ingrese primero numero"))
b=int(input("ingrese segudo numero"))
c=int(input("ingrese tercer numero"))

menor=0
intermedio=0
mayor=0
if(a<b and a<c):
    menor=menor+a
elif(b<c and b<a):
    menor=menor+b
elif(c<a and c<b):
    menor=menor+c


if(c<a<b or b<a<c):
    intermedio=intermedio+a
elif(a<b<c or c<b<a):
    intermedio=intermedio+b
elif(a<c<b or b<c<a):
    intermedio=intermedio+c

if(a>b and a>c):
    mayor=mayor+a
elif(b>a and b>c):
    mayor=mayor+b
elif(c>a and c>b):
    mayor=mayor+c

print(menor,intermedio,mayor)     