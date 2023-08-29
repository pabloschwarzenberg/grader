num1= int(input("Ingrese numero uno: "))
num2= int(input("Ingrese numero dos: "))
num3= int(input("Ingrese numero tres: "))
x= min(num1, num2, num3)
y= max(num1, num2, num3)
z= (num1 + num2 + num3) - x - y
print(x,",", z," ,", y)

