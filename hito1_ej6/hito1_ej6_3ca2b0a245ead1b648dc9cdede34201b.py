#Ordenar tres números
#Entrada
num1=int(input("Introduzca un número: "))
num2=int(input("Introduzca otro número: "))
num3=int(input("Introduzca otro número: "))

if num1>num2 and num1>num3 and  num2>num3:
  print(num3, ",",num2, ",", num1)

elif num1>num2 and num1>num3 and  num3>num2:
  print(num2, ",", num3, ",", num1)

elif num2>num1 and num2>num3 and num1>num3:
  print(num3, ",", num1, ",", num2)
  
elif num2>num1 and num2>num3 and num3>num1:
  print(num1, ",", num3, ",", num2)

elif num3>num1 and num3>num2 and num1>num2:
  print(num2, ",", num1, ",", num3)

elif num3>num1 and num3>num2 and num2>num1:
  print(num1, ",", num2, ",", num3)      
    
elif num1==num2 and  num3!= num1 and num3>num1:
  print(num1, ",", num2, ",", num3)

elif num1==num2 and num3!=num1 and num1>num3:
  print(num3, ",", num1, ",", num2)

elif num1==num3 and num2!= num1 and num2>num1:
  print(num1, ",", num3, ",", num2)

elif num1==num3 and num2!= num1 and num1>num2:
  print(num2, ",", num1, ",", num3)
        
elif num2==num3 and num1!=num2 and num1>num2:
  print(num3, ",", num2, ",", num1)
  
elif num2==num3 and num1!=num2 and num2>num1:
  print(num1, ",", num3, ",", num2)

elif num1==num2 and num2==num3:
  print(num1, ",", num2, ",", num3)      