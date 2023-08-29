a1 = int(input("Ingrese coeficiente de x de la primera ecuación: "))
b1 = int(input("Ingrese coeficiente de y de la primera ecuación: "))
c1 = int(input("Ingrese el número independiente de la primera ecuación: "))
a2 = int(input("Ingrese coeficiente de x de la segunda ecuación: "))
b2 = int(input("Ingrese coeficiente de y de la segunda ecuación: "))
c2 = int(input("Ingrese el número independiente de la segunda ecuación: "))

mdn1 = 0
mdn2 = 0

nux = max(a1, a2)
mcm = nux

while mcm % a1 != 0 or mcm % a2 != 0:
    mcm += nux

bnum = mcm

while bnum >= 0:
    bnum -= a1
    mdn1 += 1

bnum = mcm

while bnum >= 0:
    bnum -= a2
    mdn2 += 1

a3 = a1 * mdn1 - a2 * mdn2
b3 = b1 * mdn1 - b2 * mdn2
c3 = c1 * mdn1 - c2 * mdn2
if a3!=0 or b3!=0:
    x=c3/a3
y=((c1-(a1*x))/b1)
print("x=",round(x,1))
print("y=",round(y,1))