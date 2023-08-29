#descomponer un número
number = int(input("ingrese un numero: "))
newNumber = number
#encontramos la unidad
unidad = number%10
number = number//10
#encontramos la decena
decena = number%10
number = number//10
#encontramos la centena
centena = number%10
number = number//10
#encontramos la milesima
milesima = number%10
#añadimos la unidad
if 0 <= newNumber < 10:
  newNumber = str(unidad) + "U"
#añadimos la decena
if 10 <= newNumber < 100:
  answer = str(decena) + "D + " + str(unidad) + "U" 
#añadimos la centena
if 100 <= newNumber < 1000:
  answer = str(centena) + "C + " + str(decena) + "D + " + str(unidad) + "U"
#añadimos la milesima
if 1000 <= newNumber < 10000:
  answer = str(milesima) + "M + " + str(centena) + "C + " + str(decena) + "D + " + str(unidad) + "U"
#imprimimos la respuesta
print(answer)