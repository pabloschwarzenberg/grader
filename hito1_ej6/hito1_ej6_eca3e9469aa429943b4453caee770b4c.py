#Ordenar tres números
      #hacer un programa que ordene numeros de menor a mayor 

print("primer nuemro")
numero1 = int(input())
print("segundo numero")
numero2 = int(input())
print("tercer numero")
numero3 = int(input())

if(numero1<numero2 and numero2<numero3):
  print("",numero1," , ",numero2," , ",numero3)

elif(numero2<numero1 and numero1<numero3):
  print("",numero2," , ",numero1," , ",numero3)

elif(numero3<numero1 and numero1<numero2):
  print("",numero3," , ",numero1," , ",numero2)

elif(numero3<numero2 and numero2<numero1):
  print("",numero3," , ",numero2," , ",numero1)

elif(numero1<numero3 and numero3<numero2):
  print("",numero1," , ",numero3," , ",numero2)

elif(numero2<numero3 and numero3<numero1):
  print("",numero2," , ",numero3," , ",numero1)

elif(numero1==numero2 and numero2<numero3):
  print("",numero1," , ",numero2," , ",numero3)

elif(numero2==numero1 and numero1<numero3):
  print("",numero2," , ",numero1," , ",numero3)

elif(numero3==numero1 and numero1<numero2):
  print("",numero3," , ",numero1," , ",numero2)

elif(numero3==numero2 and numero2<numero1):
  print("",numero3," , ",numero2," , ",numero1)

elif(numero1==numero3 and numero3<numero2):
  print("",numero1," , ",numero3," , ",numero2)

elif(numero2==numero3 and numero3<numero1):
  print("",numero2," , ",numero3," , ",numero1)

elif(numero1==numero2 and numero2>numero3):
  print("",numero1," , ",numero2," , ",numero3)

elif(numero2==numero1 and numero1>numero3):
  print("",numero2," , ",numero1," , ",numero3)

elif(numero3==numero1 and numero1>numero2):
  print("",numero3," , ",numero1," , ",numero2)

elif(numero3==numero2 and numero2>numero1):
  print("",numero3," , ",numero2," , ",numero1)

elif(numero1==numero3 and numero3>numero2):
  print("",numero1," , ",numero3," , ",numero2)

elif(numero2==numero3 and numero3>numero1):
  print("",numero2," , ",numero3," , ",numero2)

elif(numero1==numero3 and numero3>numero2):
  print("",numero2," , ",numero1," , ",numero3)

else:
    print("numeros ordenados de menor a mayor")



