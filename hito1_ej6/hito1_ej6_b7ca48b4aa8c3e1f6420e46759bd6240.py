#Ordenar tres números
n1 = eval(input("escriba un numero entero: "))
n2 = eval(input("escriba un numero entero: "))
n3 = eval(input("escriba un numero entero: "))
a = min(n1, n2, n3)
b = max(n1, n2, n3)
c = (n1 + n2 + n3) - a - b 
print("los numeros ordenados serian",a,",",c,",",b)