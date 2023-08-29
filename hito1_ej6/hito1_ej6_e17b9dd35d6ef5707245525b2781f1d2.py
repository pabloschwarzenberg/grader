#Ordenar tres números
print("elija 3 numeros para escribirlos de menor a mayor")

a = eval(input("Elige el primer numero: "))
b = eval(input("Elige el segundo numero: "))
c = eval(input("Elige el tercer numero: "))

x = max(a,b,c)
y = min(a,b,c)
z= (a+b+c)-x-y

print("El orden de menor a mayor es",y,",",z,",",x)
