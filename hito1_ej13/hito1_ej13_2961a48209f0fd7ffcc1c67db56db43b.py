#Factores Primos
num = int(input("Ingrese numero"))
i = 2
while num !=1:
     if num%i==0:
         print(i)
         num=num/i
     else:
         i=i+1