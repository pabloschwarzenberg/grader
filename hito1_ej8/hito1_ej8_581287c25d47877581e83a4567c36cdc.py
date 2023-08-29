num=str(input("1230"))
digitos=len(str(num))
if digitos==4:
    m=num[0:1]
    c=num[1:2]
    d=num[2:3]
    u=num[3:4]
    print(m,"M + ",c,"C + ",d,"D + ",u,"U",sep="")
elif digitos==3:
    c=num[0:1]
    d=num[1:2]
    u=num[2:3]
    print(c,"C + ",d,"D + ",u,"U",sep="")
elif digitos==2:
    d=num[0:1]
    u=num[1:2]
    print(d,"D + ",u,"U",sep="")
elif digitos==1:
    u=num[0:1]
    print(u,"U",sep="")