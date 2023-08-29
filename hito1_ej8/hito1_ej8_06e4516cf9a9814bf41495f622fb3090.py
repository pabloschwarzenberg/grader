#Descomponer un número
N = int(input("introdusca un numero de 4 cifras: "))
if 0<N<10000:
  mil = N//1000 
  centena = (N%1000)//100
  decena = ((N%1000)%100)//10
  unidad = ((N%1000)%100)%10
  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")
else:
  print("un numéro con un máximo de 4 digitos")