#Descomponer un número
num = int(input("Ingrese un número de hasta 4 cifras: "))

r = num

num1 = r // 1000
r = r % 1000
num2 = r // 100
r = r % 100
num3 = r // 10
r = r % 10
num4 = r // 1
print(num1,"M+",num2,"C+",num3,"D+",num4,"U", sep='')
          
     