#Ordenar tres números

valor1 = eval(input("ingrese el primer valor: "))
valor2 = eval(input("ingrese el segundo valor: "))
valor3 = eval(input("ingrese el tercer valor: "))

if((valor1 <= valor2) and (valor1 <= valor3)):
  valor_menor = valor1
  if(valor2 <= valor3):
    valor_medio = valor2
    valor_mayor = valor3
  else:
    valor_medio = valor3
    valor_mayor = valor2
elif((valor2 <= valor1) and (valor2 <= valor3)):
  valor_menor = valor2
  if(valor1 <= valor3):
    valor_medio = valor1
    valor_mayor = valor3
  else:
    valor_medio = valor3
    valor_mayor = valor1
elif((valor3 <= valor2) and (valor3 <= valor1)):
  valor_menor = numero3
  if(valor1 <= valor2):
    valor_medio = valor1
    valor_mayor = valor2
  else:
    valor_medio = valor2
    valor_mayor = valor1
    
print(str(valor_menor) + "," + str(valor_medio) + "," + str(valor_mayor))