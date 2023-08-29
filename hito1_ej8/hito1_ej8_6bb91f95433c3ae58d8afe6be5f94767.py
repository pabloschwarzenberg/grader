a=str(input())
if(len(a) > 0):
    m=a[0]
    print(m,'U')
if(len(a) > 1):
    c=a[1]
    print(m,'D +',c,'U')
if(len(a) > 2):
    d=a[2]
    print(m,'C +',c,'D +',d,'U')
if(len(a) > 3):
    u=a[3]
    print(m,'M +',c,'C +',d,'D +',u,'U')