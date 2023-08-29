#Contestador de celular
numero=int(input("Ingrese numero telefonico:"))
hora=int(input("Ingrese hora de llamada:"))
a=numero//10000000
i=numero%10000000
b=i//1000000
j=i%1000000
c=j//100000
k=j%100000
d=k//10000
l=k%10000
e=l//1000
m=l%1000
f=m//100
n=m%100
g=n//10
h=n%10
n1=str(a)
n2=str(b)
n3=str(c)
n6=str(f)
n7=str(g)
n8=str(h)
g_1=n1+n2+n3
g_2=n6+n7+n8
if(7>=hora>=0):
    print("CONTESTAR")
elif(14>=hora>7):
    if(g_2==str(909)):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(17>hora>14):
    print("NO CONTESTAR")
elif(19>=hora>=17):
    if(g_1==str(877)):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif(24>hora>19):
    print("NO CONTESTAR")
else:
    print("Verifique si ingreso correctamente el numero y la hora")