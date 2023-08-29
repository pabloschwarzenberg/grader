#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese rut sin verificador: "))
a = rut//10000000
b = (rut%10000000)//1000000
c = (rut%1000000)//100000
d = (rut%100000)//10000
e = (rut%10000)//1000
f = (rut%1000)//100
g = (rut%100)//10
h = rut%10

s1 = h*2
s2 = g*3
s3 = f*4
s4 = e*5
s5 = d*6
s6 = c*7
s7 = b*2
s8 = a*3
sT = s1+s2+s3+s4+s5+s6+s7+s8
sTi = 11-(sT%11)

if 0<=sTi<=9:
    print("dv=",sTi)
elif sTi == 11:
    sTi = 0
    print("dv=",sTi)
elif sTi == 10:
    sTi = "K"
    print("dv=",sTi)
      