#Ordenar tres números
#Entrada
x=int(input("Inf¿grese su primer digito: "))
n=int(input("Ingrese su segundo digito: "))
m=int(input("Ingrese su ultimo digito: "))

N= min(x,n,m)
M= max(x,n,m)
E=(x+n+m)-N-M

print('el orden es: {},{},{}' . format(N,E,M))