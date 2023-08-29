#Ordenar tres números

n1 = eval(input("Ingrese el primer numero:  "))
n2 = eval(input("Ingrese el segundo numero:  "))
n3 = eval(input("Ingrese el tercer numero:  "))

mayor = max(n1 , n2 , n3)
menor = min(n1 , n2 , n3)

if (mayor > n1 > menor):
  print(menor,  "," , n1 , "," ,mayor)

elif (mayor > n2 > menor):
  print(menor,  "," , n2 , "," ,mayor)

elif (mayor > n3 > menor):
  print(menor,  "," , n3 , "," ,mayor)

elif (n1 == mayor or n1 == menor):
  print(menor,  "," , n1 , "," ,mayor)

elif (n2 == mayor or n2 == menor):
  print(menor,  "," , n2 , "," ,mayor)
  
elif (n3 == mayor or n3 == menor):
  print(menor,  "," , n3 , "," ,mayor)