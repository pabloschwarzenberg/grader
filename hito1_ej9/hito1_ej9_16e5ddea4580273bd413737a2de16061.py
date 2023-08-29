print("Ingrese los datos tal que ax + by = c\n dx + ex = f ")
lista = []
lista2 = []
lista3=[]
a = float(input("Ingrese un valor para a : "))
b = float(input("Ingrese un valor para b : "))

c = float(input("Ingrese un valor para c : "))

d = float(input("Ingrese un valor para d : "))
e = float(input("Ingrese un valor para e : "))

f = float(input("Ingrese un valor para f : "))
lista.append(((c/a)))
lista.append(((b*-1)/a))

lista2.append(((c/b)))
lista2.append((a*-1)/b)

print( a ,"x + " , b , "y = ",c ," y ", d," x + ", e ,"y = ", f )
#(lista[0]=c y lista[1]=-b)/a
x=f-(lista[0]*d)
z=(lista[1]*d)+e
w=x/z
xd=f-(lista2[0])*e
uwu=d+lista2[1]*e
aja=xd/uwu
owo="{0:.1f}".format(w)
string1=str(owo)
awa="{0:.1f}".format(aja)
string2=str(awa)
#print("Su nota final es : " ,"{0:.1f}".format(nota_final))
lista3.append("x="+string2)
lista3.append("y="+string1)
print(lista3)