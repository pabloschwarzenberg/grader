import math
rut=input("ingrese el rut sin el digito verificador ")
numero1=rut[0]
numero2=rut[1]
numero3=rut[2]
numero4=rut[3]
numero5=rut[4]
numero6=rut[5]
numero7=rut[6]
numero8=rut[7]
numero_1=int(numero1)
numero_2=int(numero2)
numero_3=int(numero3)
numero_4=int(numero4)
numero_5=int(numero5)
numero_6=int(numero6)
numero_7=int(numero7)
numero_8=int(numero8)
calculo=numero_8*2+numero_7*3+numero_6*4+numero_5*5+numero_4*6+numero_3*7+numero_2*2+numero_1*3
calculo2=calculo/11
x=math.floor(calculo2)
calculo3=abs((11*x)-calculo)
calculo4=11-calculo3
if(calculo4==11):
  dv=0
elif(calculo4==10):
  dv="k"
else:
  dv=calculo4
print("dv=",dv)