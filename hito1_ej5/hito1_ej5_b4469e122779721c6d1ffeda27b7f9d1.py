rut=int(input("ingrese un rut sin (-)y ultimo numero:"))
n8=rut%10
n7=((rut-n8)%100)/10
n6=((rut%1000)/100)-((rut%100)/100)
n5=((rut%10000)/1000)-((rut%1000)/1000)
n4=((rut%100000)/10000)-((rut%10000)/10000)
n3=((rut%1000000)/100000)-((rut%100000)/100000)
n2=((rut%10000000)/1000000)-((rut%1000000)/1000000)
n1=int(rut/10000000)
print("los numeros son",int(n8),int(n7),int(n6),int(n5),int(n4),int(n3),int(n2),int(n1))
total=(n8*2+n7*3+n6*4+n5*5+n4*6+n3*7+n2*2+n1*3)
print("total",int(total))
x=int(total/11)
final=total-x*11
print("final es",int(final))
digito=11-final
if(digito==11):
  print("dv=0")
if(digito==10):
  print("dv=k")
if(digito<10):
  print("dv=",int(digito))