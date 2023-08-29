#Descomponer un número
x=int(input("da numero de 4 digitos"))
z=x
a=z//(1000)
z=z%(1000)
b=z//(100)
z=z%(100)
c=z//(10)
z=z%(10)
d=z//(1)
z=z%(1)
e=str(a)+"M"
f=str(b)+"C"
g=str(c)+"D"
h=str(d)+"U"
w="+"
print(e+w+f+w+g+w+h)