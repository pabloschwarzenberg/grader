#Cálculo del dígito verificador de un rut
rut=(input())
lar=len(rut)

if lar==8:
    pcero=int(rut[0])
    puno=int(rut[1])
    pdos=int(rut[2])
    ptres=int(rut[3])                     
    pcuatro=int(rut[4])
    pcinco=int(rut[5])
    pseis=int(rut[6])
    psiete=int(rut[7])
    a=psiete*2
    b=pseis*3
    c=pcinco*4
    d=pcuatro*5
    e=ptres*6
    f=pdos*7
    g=puno*2
    h=pcero*3
    x=a+b+c+d+e+f+g+h
    y=x%11
    z=11-y

if lar==7:
    r="0"+rut
    pcero=int(r[0])
    puno=int(r[1])
    pdos=int(r[2])
    ptres=int(r[3])                     
    pcuatro=int(r[4])
    pcinco=int(r[5])
    pseis=int(r[6])
    psiete=int(r[7])
    a=psiete*2
    b=pseis*3
    c=pcinco*4
    d=pcuatro*5
    e=ptres*6
    f=pdos*7
    g=puno*2
    h=pcero*3
    x=a+b+c+d+e+f+g+h
    y=x%11
    z=11-y
if z==11 :
    print("dv=0")
elif z==10 :
   print("dv=k")
else:
      print("dv=",z)
