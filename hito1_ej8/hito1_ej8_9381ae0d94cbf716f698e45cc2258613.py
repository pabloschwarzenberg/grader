#Descomponer un número
Unidad = (num%10)
num//=10
Decena = (num%10)
num//= 10
Centena = (num%10)
num//=10
Miles= (num%10)
print(str(Miles)+ "M" "+" + str(Centena)+ "C" "+" + str(Decena)+ "D" "+" + str(Unidad)+"U")     