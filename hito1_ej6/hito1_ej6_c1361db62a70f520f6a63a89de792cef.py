#Ordenar tres números
num1 =int(input("Digite un numero= "))
num2 =int(input("Digite un segundo numero= "))
num3 =int(input("Digite un tercer numero= "))

if num1 <= num2 or num1 >= num2 and num1 <= num3 or num1 >= num3 and num2 <= num3 or num2 >= num3:
   if num1 <= num2:
      if num1 <= num3:
         if (num2 <= num3):
             print(num1,",",num2,",",num3)
         else:
             print(num1,",",num2,",",num3)
      else:
         print(num3,",",num1,",",num2)
   else:
      if num2 <= num3:
         if num3 <= num1:
              print(num2,",",num3,",",num1)
         else:
              print(num2,",",num1,",",num3)
      else:
          print(num3,",",num2,",",num1)
else:
    print("Sus numeros ordenados de menor a mayor son= ")
 