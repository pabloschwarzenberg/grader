#Contestador de celular
numero_de_telefono=int(input("numero de telefono: "))
z=numero_de_telefono
a=z//(10**8)
z=z%(10**8)
b=z//(10**7)
z=z%(10**7)
c=z//(10**6)
z=z%(10**6)
d=z//(10**5)
z=z%(10**5)
e=z//(10**4)
z=z%(10**4)
f=z//(10**3)
z=z%(10**3)
g=z//(100)
z=z%100
h=z//10
z=z%10
i=z//1
z=z%1
j=1*(10*(10*(10*(10*(10*(10*(10*(10*a+b)+c)+d)+e)+f)+g)+h)+i)
hora=int(input("hora: "))
x=hora
if x<=7 and x>=0:
    print("CONTESTAR")
elif x<14 and str(g)+str(h)+str(i)=="909":
        print("CONTESTAR")
elif x>=17 and x<=19 and (a!=8 and b!=7 and c!=7):
    print("CONTESTAR")
elif x>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")