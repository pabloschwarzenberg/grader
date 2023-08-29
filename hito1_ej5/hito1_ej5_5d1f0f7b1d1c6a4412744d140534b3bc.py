RUT=(input("ingrese su rut sin dato verificador: "))
num1=eval(RUT[0])
num2=eval(RUT[1])
num3=eval(RUT[2])
num4=eval(RUT[3])
num5=eval(RUT[4])
num6=eval(RUT[5])
num7=eval(RUT[6])
num8=eval(RUT[7])
suma=((num1*3)+(num2*2)+(num3*7)+(num4*6)+(num5*5)+(num6*4)+(num7*3)+(num8*2))
modulo11=(suma/11)
resto=suma-(11*modulo11)
dv=11-resto
if(dv==11):
  dv=0
elif(dv==10):
  dv="k"
 
print("dv=",dv)


