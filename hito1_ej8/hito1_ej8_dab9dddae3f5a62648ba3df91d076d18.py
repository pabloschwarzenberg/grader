#Descomponer un número
print("Hola estudiante")
num = int(input("Número natural de 1,2,3 o 4 cifras: "))

if 0<num<10000:

  mil = num//1000

  centena = (num%1000)//100

  decena = ((num%1000)%100)//10

  unidad = ((num%1000)%100)%10

  print(str(mil)+"M + "+str(centena)+"C + "+str(decena)+"D + "+str(unidad)+"U")

else:

  print("Debe ingresar un número de hasta 4 cifras como maximo")
      