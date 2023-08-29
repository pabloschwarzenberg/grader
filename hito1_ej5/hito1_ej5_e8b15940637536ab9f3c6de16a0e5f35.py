#Cálculo del dígito verificador de un rut

x = int(input('Ingrese su rut sin digito verificador:'))
mod = 11

if x < 9999999:
 a = x // 1 %10
 b = x // 10 %10
 c = x // 100 % 10
 d = x // 1000 % 10
 e = x // 10000 % 10
 f = x // 100000 % 10
 g = x // 1000000 % 10
 codigo = (a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)
elif x > 10000000:
 a = x // 1 % 10
 b = x // 10 % 10
 c = x // 100 % 10
 d = x // 1000 % 10
 e = x // 10000 % 10
 f = x // 100000 % 10
 g = x // 1000000 % 10
 h = x // 10000000 % 10
 codigo = (a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)+(h*3)

digito = mod - (codigo - (mod *(codigo//mod)))
if digito == 11:
  print('dv=0')
elif digito == 10:
 print('dv=k')
elif digito < 10:
 print('dv={}'.format(digito))