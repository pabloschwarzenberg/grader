def adn(a,n):
    
    a=a.lower()
 
    s=[]
    j=0
    for i in range(len(a)-n+1):
        s.append(a[j:j+n])
        j+=1
    list1=[]
    while s!=[]:
        o=s.pop(0)
        if o in s:
            s.remove(o)
            for y in s:
                if y==o:
                    s.remove(y)
        else:
            list1.append(o)
    d=[]
    if list1==[]:
        print("ninguna")
    else:
        for e in list1:
            print(e)
    a=a.upper()
a=input()
n=int(input())
print (adn(a,n))