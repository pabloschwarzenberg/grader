rut=int(input())
ruta=str(rut)
if 9999999<rut:
  a=ruta[7:8]
  a1=int(a)*2
  b=ruta[6:7]
  b1=int(b)*3
  c=ruta[5:6]
  c1=int(c)*4
  d=ruta[4:5]
  d1=int(d)*5
  e=ruta[3:4]
  e1=int(e)*6
  f=ruta[2:3]
  f1=int(f)*7
  g=ruta[1:2]
  g1=int(g)*2
  h=ruta[0:1]
  h1=int(h)*3
  rutsuma=int(a1+b1+c1+d1+e1+f1+g1+h1)
  div=int(rutsuma//11)
  rest=int(rutsuma-(div*11))
  total=11-rest
  if total==10:
    print("dv=k")
  elif total==11:
    print("dv=0")
  else:
      print("dv=",total)

elif rut<10000000:
    a=ruta[6:7]
    a1=int(a)*2
    b=ruta[5:6]
    b1=int(b)*3
    c=ruta[4:5]
    c1=int(c)*4
    d=ruta[3:4]
    d1=int(d)*5
    e=ruta[2:3]
    e1=int(e)*6
    f=ruta[1:2]
    f1=int(f)*7
    g=ruta[0:1]
    g1=int(g)*2
    rutsuma=int(a1+b1+c1+d1+e1+f1+g1)
    div=int(rutsuma//11)
    rest=int(rutsuma-(div*11))
    total=11-rest
    if total==10:
      print("dv=k")
    elif total==11:
      print("dv=0")
    else:
       print("dv=",total)

