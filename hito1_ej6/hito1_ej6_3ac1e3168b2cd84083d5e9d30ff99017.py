#Ordenar tres números
a= int (input("escriba el primer numero:"))
n= int(input("escriba el segundo numero:"))
m= int(input(" escriba el tercer numero:"))

b= min(a,n,m)
x= max(a,n,m)
c= (a + n + m) -b -x

print("el orden de los numeros enteros son los siguientes: {}, {}, {}". format (b,c,x))