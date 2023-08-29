num1=int(input("Dime el primer número: "))
num2=int(input("Dime el segundo número: "))
num3=int(input("Dime el tercer número: "))
valor1= min(num1,num2,num3)
valor2= max(num1,num2,num3)
valor3=(num1+num2+num3)-valor1-valor2
print("Los numeros ordenados de menor a mayor son: ",valor1,",", valor3 ,",", valor2,"Saludos!")