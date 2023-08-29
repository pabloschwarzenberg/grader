#Descomponer un número
n=eval(input())
n_string = str(n)
if n_string==3:
  a = n_string[0]
  b = n_string[1]
  c = n_string[2]
  d = n_string[3]
  print(int(a),"M+",int(b),"C+",int(c),"D+",int(d),"U",)
elif n_string==2:
  b = n_string[0]
  c = n_string[1]
  d = n_string[2]
  print(int(b),"C+",int(c),"D+",int(d),"U",)
elif n_string==2:
  c = n_string[0]
  d = n_string[1]
  print(int(c),"D+",int(d),"U",)
elif n_string==1:
  d = n_string[0]
  print(int(d),"U",)