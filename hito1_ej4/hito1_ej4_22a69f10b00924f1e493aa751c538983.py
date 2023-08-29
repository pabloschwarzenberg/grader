v1= eval(input("valor 1: "))
v2= eval(input("valor 2: "))
v3= eval(input("valor 3: "))
valores=[v1,v2,v3]
valores.sort()
print(valores)


#Suma de los N primeros números
n= int(input("numero: "))

suma= int(n*(n+1)/2)
print(suma)
print("la suma de los primeros",n, "numeros es: " ,suma)
