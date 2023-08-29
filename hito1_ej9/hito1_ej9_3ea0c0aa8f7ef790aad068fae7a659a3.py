#Sistema de Ecuaciones
#a*x1+b*y1=c"
#d*x2+e*y2=f"
#
a,b,c,d,e,f=map(int(input().split)
discriminante=(a*e)-(d*b)
if discriminante<0:
    print()
elif discriminante>=0:
    x=(c*e)-(b*f)/discriminante
    y=(a*f)-(c*d)/discriminante
    print(x,y)
    
   