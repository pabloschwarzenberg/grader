#Cálculo del dígito verificador de un rut
Rut=int(input())
number_string = str(Rut)
if Rut>9999999:
  a=number_string[0]
  b=number_string[1]
  c=number_string[2]
  d=number_string[3]
  e=number_string[4]
  f=number_string[5]
  g=number_string[6]
  h=number_string[7]
  U=int(a)*3+int(b)*2+int(c)*7+int(d)*6+int(e)*5+int(f)*4+int(g)*3+int(h)*2
  M=U%11
  L=11-M
  if (bool(0<L<10))==True:
    print("dv=",L)
  elif (bool(L==10))==True:
    print("dv=k")
  else:
    print("dv=",0)
else:
  a=number_string[0]
  b=number_string[1]
  c=number_string[2]
  d=number_string[3]
  e=number_string[4]
  f=number_string[5]
  g=number_string[6]
  U=int(a)*2+int(b)*7+int(c)*6+int(d)*5+int(e)*4+int(f)*3+int(g)*2
  M=U%11
  L=11-M
  if (bool(0<L<10))==True:
    print("dv=",L)
  elif (bool(L==10))==True:
    print("dv=k")
  else:
    print("dv=",0)



