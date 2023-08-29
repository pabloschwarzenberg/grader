n=int(input())
a=n%10
b=(n%100)//10
c=(n%1000)//100
d=(n%10000)//1000
e=(n%100000)//10000
f=(n%1000000)//100000
g=(n%10000000)//1000000
h=(n%100000000)//10000000
suma=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3
resto=suma%11
digito=11-resto
if digito==11:
    print("dv=0")
elif digito==10:
    print("dv=K")
else:
    print("dv=",digito)
      