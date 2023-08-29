num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("ingrese un numero: "))
if (num1 <= num2 and num2 <= num3):
   print(num1,",",num2,",",num3)
else:
    if (num1 <= num3 and num3<= num2):
        print(num1,",",num3,",",num2)
    else:
        if (num2 <= num1 and num1 <= num3):
            print(num2,",",num1,",",num3)
        else:
            if (num2 <= num3 and num3 <= num1):
                print(num2,",",num3,",",num1)
            else:
                if (num3 <= num1 and num1<= num2):
                    print(num3,",",num1,",",num2)
                else:
                      print(num3,",",num2,",",num1)