def sum(a,b,c,d,e,f,g,h):
    return(a+b+c+d+e+f+g+h)

rut=(int(input()))
a=rut%10
a=a*2
b=(rut%10**2-rut%10)/10
b=b*3
c=(rut%10**3-rut%10**2)/10**2
c=c*4
d=(rut%10**4-rut%10**3)/10**3
d=d*5
e=(rut%10**5-rut%10**4)/10**4
e=e*6
f=(rut%10**6-rut%10**5)/10**5
f=f*7
g=(rut%10**7-rut%10**6)/10**6
g=g*2 
h=(rut%10**8-rut%10**7)/10**7
h=h*3
digito=sum(a,b,c,d,e,f,g,h)
digito=digito%11
digito=11-digito
if digito==11:
    print("dv=0")
elif digito==10:
    print("dv=k")
elif digito<10:
    print("dv=",digito)