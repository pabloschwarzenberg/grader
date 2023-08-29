print("Ingrese 3 numeros enteros:")
n_1=int(input("Primer numero:"))
n_2=int(input("Segundo numero:"))
n_3=int(input("Tecer numero:"))
if(n_1>=n_2  and n_2>=n_3):
  print(n_3,",",n_2,",",n_1)
elif(n_2>=n_3 and n_3>=n_1):
  print(n_1,",",n_3,",",n_2)
elif(n_3>=n_1 and n_1>=n_2):
  print(n_2,",",n_1,",",n_3)
elif(n_2>=n_1 and n_1>=n_3):
  print(n_3,",",n_1,",",n_2)
elif(n_3>=n_2 and n_2>=n_1):
  print(n_1,",",n_2,",",n_3)