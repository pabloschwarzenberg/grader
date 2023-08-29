a=int(input("Ingrese el rut: "))
a=str(a)
b=[]
for c in a:
    b.append(c)
for d in range(len(a)):
    b[d]=int(b[d])
print(b)
if len(a)==8:
    nata1=b[7]*2
    nata2=b[6]*3
    nata3=b[5]*4
    nata4=b[4]*5
    nata5=b[3]*6
    nata6=b[2]*7
    nata7=b[1]*2
    nata8=b[0]*3
    nata=(nata1+nata2+nata3+nata4+nata5+nata6+nata7+nata8)
    pof=nata//11
    pof2=nata-(11*pof)
    pof1=11-pof2
    if pof1==11:
        print("dv= 0")
    elif pof1==10:
        print("dv= k")
    else:
        print("dv=",pof1)
if len(a)==7:
    nata1=b[6]*2
    nata2=b[5]*3
    nata3=b[4]*4
    nata4=b[3]*5
    nata5=b[2]*6
    nata6=b[1]*7
    nata7=b[0]*2
    nata=(nata1+nata2+nata3+nata4+nata5+nata6+nata7)
    pof=nata//11
    pof2=nata-(11*pof)
    pof1=11-pof2
    if pof1==11:
        print("dv= 0")
    elif pof1==10:
        print("dv= k")
    else:
        print("dv=",pof1)
