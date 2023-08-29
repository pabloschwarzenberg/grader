#Suma de los N primeros números
      num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
if(num1<num2):
  if(num2<num3):
    print("Los numeros en orden son: ", num1, "," , num2, ",", num3)
  elif(num2>num3):
    if(num1<num3):
      print("Los numeros en orden son: ", num1, "," , num3, "," , num2)
    elif(num3<num1):
      print("Los numeros en orden son: ", num3, "," , num1, "," , num2)
elif(num2<num1):
  if(num1<num3):
    print("Los numeros en orden son: ", num2, "," , num1, "," , num3)
  elif(num3<num1):
    if(num2>num3):
      print("Los numeros en orden son: ", num3, "," , num2, "," , num1)
    elif(num2<num3):
      print("Los numeros en orden son: ", num2, "," , num3, "," , num1)