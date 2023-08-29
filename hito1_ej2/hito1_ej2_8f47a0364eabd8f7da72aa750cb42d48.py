print("El numero de telefono debe tener solo ocho cifras y la hora debe estar entre los numeros 0 y 23")
n=int(input("Ingrese numero telefonico: "))
p=int(input("Ingrese hora de llamada: "))
a=int((n%10**8)//10**7)
b=int((n%10**7)//10**6)
c=int((n%10**6)//10**5)
d=int((n%10**5)//10**4)
e=int((n%10**4)//10**3)
f=int((n%10**3)//10**2)
g=int((n%10**2)//10)
h=int(n%10)

if 0<=p<=7:
 print("CONTESTAR")
elif 8<=p<=14 and f==9 and g==0 and h==9:
 print("CONTESTAR")

elif 17<=p<=19 and a!=8 and b!=7 and c!=7:
 print("CONSTESTAR")
else:
    print("NO CONTESTAR")  