#Cálculo del dígito verificador de un rut
n = str(input('Ingrese numero = '))

if len(n) == 8:
    p = [0,0,0,0,0,0,0,0]
elif len(n) == 7:
    p = [0,0,0,0,0,0,0]

for letra in n:
    letra = int(letra)
    p.append(letra)

p.reverse()

m = [2,3,4,5,6,7,2,3]
g = []
i = 0
while i <= 7:
    t = p[i] * m[i] 
    g.append(t)
    i = i + 1

h = sum(g)
h = h % 11
h = 11 - h

if h == 11:
    print('dv = 0')
elif h == 10:
    print('dv = K')
elif h < 10:
    print('dv =',h)
