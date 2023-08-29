#Descomponer un número
n= int(input("Adjunte cualquier número natural de 1 a 4 cifras: "))
if 0<n<10000:
  mil=n//1000
  centena=(n%1000)//100
  decena=((n%1000)%100)//10
  unidad=((n%1000)%100)%10
  print(str(mil)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")
else:
  print("tienes que ingresar un numero de menos de 4 digitos")