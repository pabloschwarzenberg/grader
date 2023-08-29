coef = [0,0,0,0,0,0]
e1 = [0,0,0]
e2 = [0,0,0]
for x in range(6):
  coef[x] = int(input("Inserte el coeficiente " + str(x) + ": "))

div1 = coef[1] 
for x in range(3):
  coef[x] = coef[x] / div1
 
e1[0] = coef[1]
e1[1] = -coef[0]
e1[2] = coef[2]

x_f = e1[1]

div2 = coef[4]
for x in range(3,6):
  coef[x] = coef[x] / div2
 
e2[0] = coef[4]
e2[1] = -coef[3]
e2[2] = coef[5]

## Ecuaciones despejadas: y = 8x + 3 ; y = 3x +1


e1[1] = e1[1] - e2[1]
e2[2] = e2[2] - e1[2]

e2[2] = e2[2] / e1[1]

x = e2[2]

y = x_f * x + e1[2]

sol = ["x=" + str(round(x,1)), "y=" + str(round(y,1))]
print(sol)