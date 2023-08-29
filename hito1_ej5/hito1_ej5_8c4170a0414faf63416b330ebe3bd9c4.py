#ENTRADA

rut=eval(input("Inserte su RUT: "))

d=(( rut // 1000000) %10 ) * 2

c=( rut // 10000000) * 3

a=(( rut // 100000) %10 ) * 7

g=(( rut // 1000) %10) * 5

e=(( rut // 10) %10) * 3

b=(( rut // 10000) %10 ) * 6

h=(( rut // 100) %10) * 4

f=(( rut // 1) %10) * 2

s=( e + g + h + d + a + f + b + c )

#PROCESAMIENTO

t1= s // 11

w2 = s - ( 11 * t1 )

p = 11 - w2

#SALIDA

if p == 10:

  print("dv=",end="")
  
  print("k")

if p == 11:

  print("dv=",end="")
  
  print(0)

else:

  print("dv=",p)
  
  print("dv=",end="")
