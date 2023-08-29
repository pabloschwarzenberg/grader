rut=input("ingresa un rut sin DV:\n")
toc=[]
for i in range(len(rut)):
    toc.append(rut[i])

x=0    
w=0
toc.reverse()
lar=len(rut)

while lar>0:
    for a in range(2,8):
        if x>=len(rut):
            break
        else:
            w+=int(toc[x])*a
            lar-=1
            x+=1
            
dv=11-(w%11)
if dv==11:
    dv=0
elif dv==10:
    dv="K"
print("dv=",dv)
