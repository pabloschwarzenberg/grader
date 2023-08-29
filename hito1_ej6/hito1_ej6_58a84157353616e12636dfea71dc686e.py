#Ordenar tres números
print("Ingresar el primer numero: ")
num1 = int(input())
print("Ingrese el segundo numero: ")
num2 = int(input())
print("Ingresar el tercer numero: ")
num3 = int(input())
if(num1>=num2 and num2>=num3):
    print(num3,",", num2,",",num1)
elif(num2>=num1 and num1>=num3):
    print(num3,",", num1,",",num2)
elif(num3>=num1 and num1>=num2):
    print(num2,",", num1,",",num3)
elif(num1>=num3 and num3>num2):
    print(num2,",", num3,",",num1)
elif(num2>=num3 and num3>=num1):
    print(num1,",", num3,",",num2)