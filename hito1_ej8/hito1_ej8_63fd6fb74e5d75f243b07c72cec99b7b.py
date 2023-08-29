#Descomponer un número
Number = int(input("Adjunte cualquier número natural de 1,2,3 o 4 cifras: "))

if 0<Number<10000:

  mil = Number//1000

  centena = (Number%1000)//100

  decena = ((Number%1000)%100)//10

  unidad = ((Number%1000)%100)%10

  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

else:

  print("un numéro con un máximo de 4 digitos")     