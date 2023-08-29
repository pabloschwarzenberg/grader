#Cálculo del dígito verificador de un rut
rut = eval(input("Ingrese su rut sin el guion: "))
a = rut % 10
b =(rut % 100 - a)//10
c = (rut % 1000 - b)//100
d = (rut % 10000 - c)//1000
e = (rut % 100000 - d)//10000
f = (rut % 1000000 - e)//100000
g = (rut % 10000000 - f)//1000000
h = ((rut % 100000000 - g)//10000000)

#sacar digitos
i = a*2
j = b*3
q = c*4
l = d*5
m = e*6
n = f*7
p = g*2
o = h*3


digitos = i + j + q + l + m + n + p + o
resto = digitos // 11
resultado = digitos - (11*resto)
final = 11- resultado

if final == 11:
  print("dv=0")
elif final == 10:
  print("dv=k")
else:
  print("dv=", final)