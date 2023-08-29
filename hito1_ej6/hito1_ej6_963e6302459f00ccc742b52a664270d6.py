#Ordenar tres números
num1=int(input("Ingrese primer valor:"))
num2=int(input("Ingrese segundo valor:"))
num3=int(input("Ingrese tercer valor:"))
if num1==num2==num3 or num1<num2<num3 or num1==num2>num3 or num2==num1>num3 or num3==num2>num1:
    print(num1,",",num2,",",num3)
elif num1<num3<num2 or num1==num3<num2 or num3==num1>num2:
    print(num1,",",num3,",",num2)
elif num2<num1<num3 or num1==num3>num2 or num3==num1<num2:
    print(num2,",",num1,",",num3)
elif num2<num3<num1 or num2==num1>num3 or num3==num2<num1:
    print(num2,",",num3,",",num1)
elif num3<num1<num2 or num1==num2<num3 or num2==num1<num3:
    print(num3,",",num1,",",num2)
elif num3<num2<num1 or num2==num1<num3 or num3==num2<num1:
    print(num3,",",num2,",",num1)