#Descomponer un número
NC = str(input("ingrese un numero de hasta 4 digitos: "))

LN = list(NC)
X = len(LN)

if X >= 1:
  LN[-1] += "U"

if X >= 2:
  LN[-2] += "D"

if X >= 3:
  LN[-3] += "C"

if X == 4:
  LN[-4] += "M"
  
SF = " + ".join(LN)
print(SF)