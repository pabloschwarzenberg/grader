#Cálculo del dígito verificador de un rut #Benjamín Araya
print("SI SU NUMERO TERMINA EN K REMPLZE K POR 0")
numero = int(input("Ingresa un rut: "))
#Separador de cafa número número= numero % 10


a = int(numero / 10)
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

#Impresión de cafa número
print(a,b,c,d,e,f,g,h)

#OPERACION DE CADA NÚMERO POR SEPARADO
ap=a*2
bp=b*3
cp=c*4
dp=d*5
ep=e*6
fp=f*7
gp=g*2
hp=h*3

#Suma de los resultados


resultados=ap+bp+cp+dp+ep+fp+gp+hp
operacion=int(resultados/11)

#digito
qw=resultados-(operacion*11)
w=11-qw

#calculo dv
if(w==11):
  print("dv=",(int(0)))
elif(w==10):
  print("dv=K")
else:
  print("dv=",w)
