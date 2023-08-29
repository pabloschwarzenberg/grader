#Cálculo del dígito verificador de un rut
rut = int(input())
dig1= rut%10
dig2= (rut//10)%10
dig3= (rut//100)%10
dig4= (rut//1000)%10
dig5= (rut//10000)%10
dig6= (rut//100000)%10
dig7= (rut//1000000)%10
dig8= (rut//10000000)%10
dig1=dig1*2
dig2=dig2*3
dig3=dig3*4
dig4=dig4*5
dig5=dig5*6
dig6=dig6*7
dig7=dig7*2
dig8=dig8*3
cv= dig1+dig2+dig3+dig4+dig5+dig6+dig7+dig8
cv1= cv // 11
cv= cv - (cv1*11)
cv=11 - cv
if cv==11:
    print("dv=0")
elif cv==10:
    print("dv=k")
else:
    print("dv=",cv)