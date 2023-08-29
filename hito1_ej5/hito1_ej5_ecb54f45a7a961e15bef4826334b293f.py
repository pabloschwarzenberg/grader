a=input()
if len(a)==7:
    a="0"+a
digito_1=str(a)[0]
digito_2=str(a)[1]
digito_3=str(a)[2]
digito_4=str(a)[3]
digito_5=str(a)[4]
digito_6=str(a)[5]
digito_7=str(a)[6]
digito_8=str(a)[7]
b=int(digito_8)*2
c=int(digito_7)*3
d=int(digito_6)*4
e=int(digito_5)*5
f=int(digito_4)*6
g=int(digito_3)*7
h=int(digito_2)*2
i=int(digito_1)*3
suma=b+c+d+e+f+g+h+i
k=suma%11
resta=11-k
if resta==11:
    print("dv=0")
elif resta==10:
    print("dv=k")
else:
    print("dv=",resta)