sec=str(input("Secuencia: "))
n=int(input("Largo de subsecuencias: "))
secl=list(sec)
subs=[]
subst=[]

for i in secl:
    c=0
    
    j=secl.index(i)
    while c<n and secl.index(i)<=(len(sec)-n-1):
        sc=secl.copy()
        sd=sc.copy()
        subs.append(sc[j])
        c+=1
        j+=1
        if n==len(subs):
            s="".join(subs)
            subst.append(s)
            subs.clear()
            continue
        else:
            continue
            
        
#n=3 -->2
#n=2--->1
#n=1--->0    
x=subst[0:-(n-1)]        
repeticiones=[]         
for a in x :
    if x.count(a)==1 :
        repeticiones.append(a)
    else:
        continue
print(repeticiones)
if repeticiones==[]:
    print("ninguna")
else:
    for t in repeticiones:
        print(repeticiones.pop(repeticiones.index(t)))
    

        

