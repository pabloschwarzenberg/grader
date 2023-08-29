#Descomponer un número
n=str(input())   
z=len(n)

N=n

if z==1:
  a=N[0]
  print(a+"U")
elif z==2:
  a=N[0]
  b=N[1]
  print(b+"U+"+a+"D")
elif z==3:
  a=N[0]
  b=N[1]
  c=N[2]
  print(a+"C+"+b+"D+"+c+"U")
elif z==4:
  a=N[0]
  b=N[1]
  c=N[2]
  d=N[3]
  print(a+"M+"+b+"C+"+c+"D+"+d+"U")     