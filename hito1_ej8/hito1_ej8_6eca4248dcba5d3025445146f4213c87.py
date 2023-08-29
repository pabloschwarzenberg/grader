#Descomponer un número
z=int(input("ingrese numero:"))
a=int(z//1000)
b=int((z-1000*a)//100)
c=int(z-1000*a-100*b)//10
d=int(z-1000*a-100*b-10*c)
print(str(a)+"M","+",str(b)+"C","+",str(c)+"D","+",str(d)+"U")


      