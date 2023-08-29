#Ordenar tres números
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))
numero3 = int(input("ingrese el tercer numero: "))
coma = ","
#sacar el orden de los numeros de menor a mayor
if numero1 <= numero2 <= numero3:
  print(numero1,coma,numero2,coma,numero3  )            
elif numero1 <= numero3 <= numero2:
  print(numero1,coma,numero3,coma,numero2  ) 
elif numero2 <= numero1 <= numero3:
  print(numero2,coma,numero1,coma,numero3  )
elif numero2 <= numero3 <= numero1:
  print(numero2,coma,numero3,coma,numero1  )
elif numero3 <= numero1 <= numero2:
  print(numero3,coma,numero1,coma,numero2  )
elif numero3 <= numero2 <= numero1:
  print(numero3,coma,numero2,coma,numero1  )  