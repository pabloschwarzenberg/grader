x=int(input('Ingresa un número de maximo 4 digitos:'))


m=x//1000
c=x%1000
c=c//100
d=x%100
d=d//10
u=x%10

if 0<=x<10:
    SINe=str(u)+'U'
    print(SINe)
    
if 10<=x<100:
    SINespacio=str(d)+'D'+'+'+str(u)+'U'
    print(SINespacio)
if 100<=x<1000:
    SINespacio=str(c)+'C'+'+'+str(d)+'D'+'+'+str(u)+'U'
    print(SINespacio)
if 1000<=x<10000:
    SINespacio=str(m)+'M'+'+'+str(c)+'C'+'+'+str(d)+'D'+'+'+str(u)+'U'
    print(SINespacio)