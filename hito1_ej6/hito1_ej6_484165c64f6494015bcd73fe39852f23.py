#Ordenar tres números
print("Eliga tres números a ser comparados.")
n1 = int(input())
n2 = int(input())
n3 = int(input())
if n1 <= n2 <= n3:
  print("El orden de menor a mayor es:", n1 ,",", n2 ,",", n3,".")
elif n1 <= n3 <= n2:
  print("El orden de menor a mayor es:", n1 ,",", n3 ,",", n2,".")
elif n2 <= n1 <= n3:
  print("El orden de menor a mayor es:", n2 ,",", n1 ,",", n3,".")
elif n2 <= n3 <= n1:
  print("El orden de menor a mayor es:", n2 ,",", n3 ,",", n1,".")
elif n3 <= n2 <= n1:
  print("El orden de menor a mayor es:", n3 ,",", n2 ,",", n1,".")
elif n3 <= n1 <= n2:
  print("El orden de menor a mayor es:", n3 ,",", n1 ,",", n2,".")