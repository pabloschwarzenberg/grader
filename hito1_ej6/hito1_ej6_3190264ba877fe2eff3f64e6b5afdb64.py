#Ordenar tres números
var_1 = int(input("escriba un numero: "))
var_2 = int(input("escriba un numero: "))
var_3 = int(input("escriba un numero: "))
if var_1 <= var_2 and var_2 <= var_3:
  print(var_1 ,",", var_2 ,",", var_3)
elif var_1 <= var_3 and var_3 <= var_2:
  print(var_1 ,",", var_3 ,",", var_2)
elif var_2 <= var_1 and var_1 <= var_3:
  print(var_2 ,",", var_1 ,",", var_3)
elif var_2 <= var_3 and var_3 <= var_1:
  print(var_2 ,",", var_3 ,",", var_1)
elif var_3 <= var_1 and var_1 <= var_2:
  print(var_3 ,",", var_1 ,",", var_2)
else:
  print(var_3 ,",", var_2 ,",", var_1)