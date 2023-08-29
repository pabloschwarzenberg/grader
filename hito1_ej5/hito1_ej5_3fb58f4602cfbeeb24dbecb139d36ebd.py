#Cálculo del dígito verificador de un rut
n=int(input())
n_1=(n//10000000)
n_2=((n//1000000)-((n//10000000)*10))
n_3=(n//100000)-((n//1000000)*10)
n_4=(n//10000)-((n//100000)*10)
n_5=((n%10000)-(n%1000))//1000
n_6=((n%1000)-(n%100))//100
n_7=((n%100)-(n%10))//10
n_8=(n%10)
suma=(n_8*2)+(n_7*3)+(n_6*4)+(n_5*5)+(n_4*6)+(n_3*7)+(n_2*2)+(n_1*3)
r=suma%11
digito= 11-r
if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=K")
else:
  print("dv="+str(digito))