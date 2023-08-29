n=int(input("ingrese su rut sin -:"))
x=n%10
y=((n-x)%100)/10
z=((n%1000)/100)-((n%100)/100)
c=((n%10000)/1000)-((n%1000)/1000)
v=((n%100000)/10000)-((n%10000)/10000)
b=((n%1000000)/100000)-((n%100000)/100000)
a=((n%10000000)/1000000)-((n%1000000)/1000000)
m=int(n/10000000)
print("sus numeros son",int(x),int(y),int(z),int(c),int(v),int(b),int(a),int(m))
total = ( x*2 + y*3 + z*4 + c*5 + v*6 + b*7 + a*2 + m*3)
print("total",int(total))
r=int(total/11)
final=total-r*11
print("final es",int(final))
digito=11-final
if(digito==11):
  print("dv=0")
if(digito==10):
  print("dv=k")
if(digito<10):
  print("dv=",int(digito))