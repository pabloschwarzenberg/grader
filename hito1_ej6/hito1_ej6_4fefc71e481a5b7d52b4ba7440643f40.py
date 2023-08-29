#Ordenar tres números
#Ej:Numeros a elegir 1,2,3,4,5,6...

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
c = int(input("ingrese el tercero numero: "))

mayor, medio, menor= 0,0,0
if a>b and a>c:
      mayor=a
      if b>c:
          medio,menor=b,c
      else:
          medio,menor=c,b
elif b>a and b>c:
      mayor=b
      if a>c:
          medio,menor=a,c
      else:
          medio,menor=c,a
else: 
      mayor=c
      if a>b:
          medio,menor=a,b
      else:
          medio,menor=b,a

print("los numeros ordenados son:{},{},{}".format(menor,medio,mayor))

   