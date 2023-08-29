#Ordenar tres números
num01= int(input("Escriba el primero numero: "))
num02= int(input("Escriba el segundo numero: "))
num03= int(input("Escriba el tercer numero: "))
numeros=num01,num02,num03

a= min(num01, num02, num03)
b= max(num01, num02, num03)
c= (num01+num02+num03)- a - b

print("Los nùmeros ordenados de menor a mayor son: {}, {}, {}" .format (a,c,b))