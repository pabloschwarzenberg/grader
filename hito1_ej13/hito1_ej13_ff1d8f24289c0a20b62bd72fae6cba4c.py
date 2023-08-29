#Factores Primos
num = input("Ingrese número: ")
num = int(num)
print("Sus factores primos son: ")
i = 2
while (i * i <= num):
  if(num%i==0): 
    print("  ",i)
  while num % i == 0:
    num = num / i
  i = i + 1
print("  ",int(num))
