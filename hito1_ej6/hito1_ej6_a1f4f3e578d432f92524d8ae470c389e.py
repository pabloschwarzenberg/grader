#Ordenar tres números
N1=int(input("Ingrese el primer numero"))
N2=int(input("ingrese el segundo numero"))
N3=int(input("ingrese el tercer numero"))
if (N1>=N2 and N2>=N3 and N1>=N3):
  print ("estos son los numeros", N3,",", N2, ",", N1) 
elif (N2>=N1 and N2>=N3 and N1>=N3):
  print ("estos son los numeros", N3,",", N1, ",", N2 )
elif (N3>=N1 and N3>=N2 and N2>=N1):
  print("estos son los numeros", N1,",", N2, ",", N3)
elif (N2>=N3 and N3>=N1 and N2>=N1):
  print ("estos son los numeros", N1,",", N3, "," , N2)
elif (N1>=N2 and N3>=N2 and N3>=N1):
  print ("estos son los numeros", N2,"," ,N1,",",N3)
elif (N1>=N3 and N1>=N2 and N3>=N2):
  print ("estos son los numeros", N2,",", N3, ",",N1)