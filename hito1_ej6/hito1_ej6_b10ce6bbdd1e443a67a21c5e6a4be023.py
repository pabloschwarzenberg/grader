#Ordenar tres número
a = int(input("ingresa un numero"))
b = int(input("ingresa otro digito"))
c = int(input("ingresa un nuevo valor"))
X = min(a,b,c)
Z = max(a,b,c)
Y = (a+b+c)-X-Z
print("los numeros ordenados son {},{},{}".format(X,Y,Z))
#:)