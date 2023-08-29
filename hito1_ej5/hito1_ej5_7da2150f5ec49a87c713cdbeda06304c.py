rut=int(input("Rut sin digito verificador: "))
n1=int(rut//(10**7))
n2=int((rut//(10**6))-(n1*10))
n3=int((rut//(10**5))-(n1*100+n2*10))
n4=int((rut//(10**4))-(n1*1000+n2*100+n3*10))
n5=int((rut//(10**3))-(n1*10000+n2*1000+n3*100+n4*10))
n6=int((rut//(10**2))-(n1*100000+n2*10000+n3*1000+n4*100+n5*10))
n7=int((rut//(10**1))-(n1*1000000+n2*100000+n3*10000+n4*1000+n5*100+n6*10))
n8=int((rut//(10**0))-(n1*10000000+n2*1000000+n3*100000+n4*10000+n5*1000+n6*100+n7*10))
m1=int(rut//(10**6))
m2=int((rut//(10**5))-(m1*10))
m3=int((rut//(10**4))-(m1*100+m2*10))
m4=int((rut//(10**3))-(m1*1000+m2*100+m3*10))
m5=int((rut//(10**2))-(m1*10000+m2*1000+m3*100+m4*10))
m6=int((rut//(10**1))-(m1*100000+m2*10000+m3*1000+m4*100+m5*10))
m7=int((rut//(10**0))-(m1*1000000+m2*100000+m3*10000+m4*1000+m5*100+m6*10))
s1=int(2*n8+3*n7+4*n6+5*n5+6*n4+7*n3+2*n2+3*n1)
d1=int(s1//11)
r1=int(s1-(11*d1))
f1=int(11-r1) 
s2=int(2*m7+3*m6+4*m5+5*m4+6*m3+7*m2+2*m1)
d2=int(s2//11)
r2=int(s2-(11*d2))
f2=int(11-r2) 
if rut>99999999:
 print("Incorrecto")
elif 9999999<rut<=99999999 and f1==11:
 print("dv=0")
elif rut<=99999999 and f1==10:
 print("dv=K")
elif rut<=99999999 and f1<10:
 print("dv=",f1)
elif rut<=9999999 and f2==11:
 print("dv=0")
elif rut<=99999999 and f2==10:
 print("dv=K")
elif rut<=99999999 and f2<10:
 print("dv=",f2)
    