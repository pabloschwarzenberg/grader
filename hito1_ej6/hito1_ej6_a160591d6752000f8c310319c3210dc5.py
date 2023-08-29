#Ordenar tres números
print("A continuación, se le pedirá digitar tres números enteros. El programa los ordenará de menor a mayor.")
num1=int(input("Digite el primer número: "))
num2=int(input("Digite el segundo número: "))
num3=int(input("Digite el tercer número: "))
if num1==num2 and num2==num3:
    print("Los tres números son idénticos.")
elif num1<=num2 and num2<=num3:
    print(num1,",",num2,",",num3)
elif num1<=num3 and num3<=num2:
    print(num1,",",num3,",",num2)
elif num2<=num1 and num1<=num3:
    print(num2,",",num1,",",num3)
elif num2<=num3 and num3<=num1:
    print(num2,",",num3,",",num1)
elif num3<=num1 and num1<=num2:
    print(num3,",",num1,",",num2)
elif num3<=num2 and num2<=num1:
    print(num3,",",num2,",",num1)