print("Ingrese su rut sin digito verificador ni puntos ej: 12345678")
rut = int(input("Ingrese su rut "))
a = rut // 10000000
b = rut // 1000000
c = b % 10
d = rut // 100000
e = d % 10
f = rut // 10000
g = f % 10
h = rut // 1000
i = h % 10
j = rut // 100
k = j % 10
l = rut // 10
m = l % 10
n = rut // 1
o = n % 10

a1 = o * 2
a2 = m * 3
a3 = k * 4
a4 = i * 5
a5 = g * 6
a6 = e * 7
a7 = c * 2
a8 = a * 3
r = a1+a2+a3+a4+a5+a6+a7+a8
r2 = r / 11
r3 = r2 // 1
r4 = r3 * 11
r5 = r - r4
r6 = 11 - r5
r7 = r6 // 1

if r7 >= 11:
  print("dv=0")
elif r7 == 10:
  print(" dv=k")
elif (r7 >= 1 or r7 <= 9):
  print("dv=",r7)