#Suma de los N primeros números
N=int(input("ingrese un numero natural N para la suma de los primeros N terminos:" ))
if(N<int(0)):
  print("error:\"el numero ingresado no es natural\" ")
  print("intente nuevamente")
  #codigo para volver a la linea 2??
else:
  S=int((N*(N+1))/2)
  print("La suma de los primeros",N,"numeros naturales es:",str(S)+".")