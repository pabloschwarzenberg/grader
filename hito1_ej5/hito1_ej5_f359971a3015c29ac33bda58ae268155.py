#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut sin digito verificador: "))
n1=(rut - (rut%10000000))
d1=(n1/10000000)
res1=rut-n1
n2=res1 -(rut%1000000)
d2=n2/1000000
res2= res1-n2
n3=res2 -(rut%100000)
d3=n3/100000
res3= res2-n3
n4=res3 -(rut%10000)
d4=n4/10000
res4=res3-(n4)
n5=res4-(rut%1000)
d5=n5/1000
res5=res4-n5
n6=res5-(rut%100)
d6=n6/100
res6=res5-n6
n7=res6-(rut%10)
d7=n7/10
res7=res6-n7
n8=res7-(rut%1)
d8 = n8/1
suma = (d8*2+d7*3+d6*4+d5*5+d4*6+d3*7+d2*2+d1*3)
dv= 11 - (suma%11)
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=K")
elif dv!=11 and dv!=10:
    print("dv=",dv)
