numero = int(input("Ingresa un rut: "))

#numeros

a = numero % 10
numero = int(numero / 10)
b = numero % 10
numero = int(numero / 10)
c = numero % 10
numero = int(numero / 10)
d = numero % 10
numero = int(numero / 10)
e = numero % 10
numero = int(numero / 10)
f = numero % 10
numero = int(numero / 10)
g = numero % 10
numero = int(numero / 10)
h = numero % 10
numero = int(numero / 10)

#orden numeros 

print(a,b,c,h,e,f,g,h)

#operatoria

ap=a*2
bp=b*3
cp=c*4
dp=d*5
ep=e*6
fp=f*7
gp=g*2
hp=h*3

#suma de resutlados

pp=ap+bp+cp+dp+ep+fp+gp+hp
op=int(pp/11)

#digito

qw=pp-(op*11)
w=11-qw

#calculo digito verificador 

if(w==11):
  print("dv=",(int(0)))
elif(w==10):
  print("dv=K")
else:
  print("dv=",w)
