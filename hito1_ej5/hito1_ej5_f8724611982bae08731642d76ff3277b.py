#Cálculo del dígito verificador de un rut

rut=int(input())
if rut//10000000<0:
    c1=rut//1000000
    c2=(rut//100000)%10
    c3=(rut//10000)%10
    c4=(rut//1000)%10
    c5=(rut//100)%10
    c6=(rut//10)%10
    c7=(rut%10)
    suma=c1*2+c2*7+c3*6+c4*5+c5*4+c6*3+c7*2
    resto=suma%11
    dv=11-resto
else:
    c1=rut//10000000
    c2=(rut//1000000)%10
    c3=(rut//100000)%10
    c4=(rut//10000)%10
    c5=(rut//1000)%10
    c6=(rut//100)%10
    c7=(rut//10)%10
    c8=(rut%10)
    suma=c1*3+c2*2+c3*7+c4*6+c5*5+c6*4+c7*3+c8*2
    resto=suma%11
    dv=(11-resto)
         
if dv==11:
  print("dv=0")
if dv==10:
  print("dv=k")
else:
  print("dv=",dv)

