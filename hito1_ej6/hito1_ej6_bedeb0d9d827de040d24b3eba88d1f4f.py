#Ordenar tres números
num1 = int(input('ingrese primer numero: '))     
num2 = int(input('ingrese segundo numero: '))   
num3 = int(input('ingrese tercer numero: '))   

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
      print(num3,",",num2,",",num1)
    else:
      print(num2,",",num3,",",num1)
    
if num2 >= num1 and num2 >= num3:
    if num1 >= num3:
      print(num3,",",num1,",",num2)  
    else:
      print(num1,num3,num2)
if num3 >= num2 and num3 >= num1:
    if num2 >= num1:
      print(num1,",",num2,",",num3)
    else:
      print(num2,",",num1,",",num3)