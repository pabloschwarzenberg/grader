#Ordenar tres números
num1=int(input(""))
num2=int(input(""))
num3=int(input(""))
if num1>=num2:
    if num1>=num3:
        if num2>=num3:
            print(num3,",",num2,",",num1)
        else:
            print(num2,",",num3,",",num1)
    elif num3>=num1:
        print(num2,",",num1,",",num3)
elif num2>=num1:
    if num2>=num3:
        if num3>=num1:
            print(num1,",",num3,",",num2)
        else:
            print(num3,",",num1,",",num2)
    elif num3>=num2:
        print(num1,",",num2,",",num3)
