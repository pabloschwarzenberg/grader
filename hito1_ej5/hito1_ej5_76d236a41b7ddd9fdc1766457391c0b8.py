rut=int(input('Ingrse rut: '))
d1=rut%10
a=rut//10
d2=a%10
b=a//10
d3=b%10
c=b//10
d4=c%10
d=c//10
d5=d%10
e=d//10
d6=e%10
f=e//10
d7=f%10
g=f//10
d8=g%10
suma=(d1*2)+(d2*3)+(d3*4)+(d4*5)+(d5*6)+(d6*7)+(d7*2)+(d8*3)
resto=suma%11
total=11-resto
if total==11:
    print('dv=0')
elif total==10:
    print('dv=K')
elif total!=11 and total!=10:
    print('dv=', total)