e = eval(input("ingrese numero rut: "))
c1 = e % 10
c2 = int((e % 100) / 10)
c3 = int((e % 1000) / 100)
c4 = int((e % 10000) / 1000)
c5 = int((e % 100000) / 10000)
c6 = int((e % 1000000) / 100000)
c7 = int((e % 10000000) / 1000000)
c8 = int((e - (e % 10000000)) / 10000000)
n = c1 * 2
u = c2 * 3
m = c3 * 4
e = c4 * 5
r = c5 * 6
a = c6 * 7
d = c7 * 2
o = c8 * 3
variable = n + u + m + e + r + a + d + o
variable1 = variable % 11
variable2 = int(11 - variable1)
if variable2 == 11:
    print("dv=0")
if variable2 == 10:
    print("dv=k")
else :
    print("dv=", variable2)