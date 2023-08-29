numero=str(input("Ingrese un numero de cuatro digitos: "))
cuatro= list(numero)
n=len(cuatro)
if n == 4 : 
  U =int(list (numero)[3]) 
  D= int (list(numero)[2])
  C= int(list(numero)[1])
  M= int(list(numero)[0])
  print(M,"M + ", C, "C +", D, "D +", U, "U")
if n == 2:
  D =int(list(numero)[1]) 
  U=int (list(numero)[0]) 
  print(D,"D +", U, "U")
if n == 3: 
  C=int(list(numero)[0])
  D=int(list(numero)[1])
  U=int(list(numero)[2])
  print(C, "C+ ", D, "D +", U , "U" )
if n==1:
  U=int(list(numero)[0])
  print(U,"U")