numeros = input("ingrese los coeficientes de las dos ecuaciones: ")
coef = ""

for a in numeros:
  if a == " ":
    pass
  else:
    coef += a

ecuacion1 = []
ecuacion2 = []

for a in range(len(coef)):
  if a < 3:
    ecuacion1.append(coef[a])
  else:
    ecuacion2.append(coef[a])



a = int(ecuacion1[0])
b = int(ecuacion1[1])
c = int(ecuacion1[2])

d = int(ecuacion2[0])
e = int(ecuacion2[1])
f = int(ecuacion2[2])

y = ((c * d) - (a * f)) / ((b * d) - (a * e))
x = ((c * e) - (b * f)) / ((a * e) - (b * d))

print(x)
print(y)