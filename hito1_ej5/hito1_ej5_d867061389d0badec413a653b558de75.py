#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut sin su número verificador: "))
n1=rut//10000000
n11=(rut-n1*10000000)
n2=n11//1000000
n22=(rut-n1*10000000-n2*1000000)
n3=n22//100000
n33=(rut-n1*10000000-n2*1000000-n3*100000)
n4=n33//10000
n44=(rut-n1*10000000-n2*1000000-n3*100000-n4*10000)
n5=n44//1000
n55=(rut-n1*10000000-n2*1000000-n3*100000-n4*10000-n5*1000)
n6=n55//100
n66= (rut-n1*10000000-n2*1000000-n3*100000-n4*10000-n5*1000-n6*100)
n7=n66//10
n77= (rut-n1*10000000-n2*1000000-n3*100000-n4*10000-n5*1000-n6*100-n7*10)
n8=n77


r1=n8*2
r2=n7*3
r3=n6*4
r4=n5*5
r5=n4*6
r6=n3*7
r7=n2*2
r8=n1*3

r=r1+r2+r3+r4+r5+r6+r7+r8
rr=11-(r%11)
if 11-(r%11)==11:
    print("dv=0")
elif 11-(r%11)==10:
    print("dv=K")
else:
    print("dv=",rr)
