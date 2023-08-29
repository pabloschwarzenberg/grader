#Cálculo del dígito verificador de un rut
n=str(input("Ingrese RUT:"))
m=len(n)-1
if m==7:
    b=int(int(n[m])*2+int(n[m-1])*3+int(n[m-2])*4+int(n[m-3])*5+int(n[m-4])*6+int(n[m-5])*7+int(n[m-6])*2+int(n[m-7])*3)
    c=b%11
    d=11-c
    if d!=10 and d!=11:
        print("dv=",d)
    elif d==10:
        print("dv=K")
    elif d==11:
        print("dv=0")
elif m==6:
    b=int(int(n[m])*2+int(n[m-1])*3+int(n[m-2])*4+int(n[m-3])*5+int(n[m-4])*6+int(n[m-5])*7+int(n[m-6])*2)
    c=b%11
    d=11-c
    if d!=10 and d!=11:
        print("dv=",d)
    elif d==10:
        print("dv=K")
    elif d==11:
        print("dv=0")
      