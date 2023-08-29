#Factores Primos

b=raw_input('  ingrese un numero ==> ') 
print 
primo=b 
l=[] 
x=0 
primo=int(primo) 
while primo%2==0: 
    x=x+1 
    primo=primo/2 
if x>0: 
    l.append(2) 
    l.append(x) 
x=0 
pri=primo 
primo=int(primo**0.5)+1 
for i in range(3,primo,2): 
    while pri%i==0: 
        x=x+1 
        pri=pri/i 
    if x>0: 
        l.append(i) 
        l.append(x) 
        x=0 
if pri>primo: 
    l.append(pri) 
    l.append(1) 
a='' 
i=0 
con=0 
while i<len(l): 
    con=con+l[i+1]+1 
    if a!="": a=a+' x ' 
    if l[i+1]==1: 
        a=a+str(l[i]) 
    else: 
        a=a+str(l[i])+'^'+str(l[i+1]) 
    i=i+2 
if a==b: 
    print '  %s es un numero primo'%a 
else:         
    print '  %s se descompone en ' %b + a 
    print 
    print '  El numero de divisores de %s es %i'%(b,con)