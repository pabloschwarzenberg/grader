rut=(input())
largo=len(rut)

if largo==8:
    a1=int(rut[0])
    a2=int(rut[1])
    a3=int(rut[2])
    a4=int(rut[3])                     
    a5=int(rut[4])
    a6=int(rut[5])
    a7=int(rut[6])
    a8=int(rut[7])
    a=a8*2
    b=a7*3
    c=a6*4
    d=a5*5
    e=a4*6
    f=a3*7
    g=a2*2
    h=a1*3
    x=a+b+c+d+e+f+g+h
    y=x%11
    z=11-y

if largo==7:
    r="0"+rut
    a1=int(r[0])
    a2=int(r[1])
    a3=int(r[2])
    a4=int(r[3])                     
    a5=int(r[4])
    a6=int(r[5])
    a7=int(r[6])
    a8=int(r[7])
    a=a8*2
    b=a7*3
    c=a6*4
    d=a5*5
    e=a4*6
    f=a3*7
    g=a2*2
    h=a1*3
    x=a+b+c+d+e+f+g+h
    y=x%11
    z=11-y
if z==11 :
    print("dv=0")
elif z==10 :
   print("dv=k")
else:
      print("dv=",z)