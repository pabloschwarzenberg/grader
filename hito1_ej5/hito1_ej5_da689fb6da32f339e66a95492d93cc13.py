#Cálculo del dígito verificador de un rut
  rut=int(input("ingrese su rut: "))
a=rut//10000000
b=rut//1000000
c=rut//100000
d=rut//10000
e=rut//1000
f=rut//100
g=rut//10
h=rut//1
a2=float(a)
b2=float(b)
c2=float(c)
d2=float(d)
e2=float(e)
f2=float(f)
g2=float(g)
h2=float(h)
calculo1= a2*2+b2*3+c2*4+d2*5+e2*6+f2*7+g2*2+h2*3
calculo2=int(calculo1/11)
calculo3=int((calculo1-(11*calculo2)))
calculo4=11-calculo3
if (calculo4==11):
    print("su digito verificador es 0")
elif(calculo4==10):
    print("su digito verificador es K")
else:
    print("su digito verificador es:",calculo4)
              
