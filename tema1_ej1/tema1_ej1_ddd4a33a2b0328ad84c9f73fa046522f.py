#Suma de los N primeros números
n= int(input("ingrese n:"))
while not(n>0):
    n= int(input("ingrese n:"))
suma= n*(n+1)/2
print("la suma de los n primeros es:", n, "numero es:", suma)  