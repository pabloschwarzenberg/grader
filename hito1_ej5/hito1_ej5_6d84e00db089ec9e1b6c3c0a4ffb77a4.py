numero = int(input("Ingresa un rut: "))
#sacar cada numero
l = numero % 10
numero = int(numero / 10)
k = numero % 10
numero = int(numero / 10)
j = numero % 10
numero = int(numero / 10)
h = numero % 10
numero = int(numero / 10)
g = numero % 10
numero = int(numero / 10)
f = numero % 10
numero = int(numero / 10)
d = numero % 10
numero = int(numero / 10)
s = numero % 10
numero = int(numero / 10)
#numeros
print(l,k,j,h,g,f,d,s)
#operacion
lp=l*2
kp=k*3
jp=j*4
hp=h*5
gp=g*6
fp=f*7
dp=d*2
sp=s*3
#suma de resutlados
pp=lp+kp+jp+hp+gp+fp+dp+sp
op=int(pp/11)
#digito
qw=pp-(op*11)
w=11-qw
#calculo dv
if(w==11):
  print("dv=",(int(0)))
elif(w==10):
  print("dv=K")
else:
  print("dv=",w)
      