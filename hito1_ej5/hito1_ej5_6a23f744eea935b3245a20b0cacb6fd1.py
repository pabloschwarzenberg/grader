#Cálculo del dígito verificador de un rut
rut= input("ingesa tu numero de rut sin digito verificador: ")
num1= rut[-8]
num2= rut[-7]
num3= rut[-6]
num4= rut[-5]
num5= rut[-4]
num6= rut[-3]
num7= rut[-2]
num8= rut[-1]
rut1= int(num1)
rut2= int(num2)
rut3= int(num3)
rut4= int(num4)
rut5= int(num5)
rut6= int(num6)
rut7= int(num7)
rut8= int(num8)
suma_productos= (rut8*2)+(rut7*3)+(rut6*4)+(rut5*5)+(rut4*6)+(rut3*7)+(rut2*2)+(rut1*3)
parte_entera= int(suma_productos/11)//1
resto= suma_productos - (parte_entera*11)
digver= 11 - resto
if digver == 11:
  print("dv: 0")
elif digver == 10:
  print("dv: k")
else:
  print("dv:", digver)      