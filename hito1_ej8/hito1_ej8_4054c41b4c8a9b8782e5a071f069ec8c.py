#Descomponer un número
num=input('')
a=''
b=''
c=''
d=''
if len(num)==4:
    a=num[0]+'M'
    b=num[1]+'C'
    c=num[2]+'D'
    d=num[3]+'U'
    print(a,'+',b,'+',c,'+',d)
elif len(num)==3:
    a=num[0]+'C'
    b=num[1]+'D'
    c=num[2]+'U'
    print(a,'+',b,'+',c)
elif len(num)==2:
    a=num[0]+'D'
    b=num[1]+'U'
    print(a,'+',b)
else:
    a=num[0]+'U'
    print(a)
