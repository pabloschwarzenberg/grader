rut =input("RUT porfa : ")
S=0
M=2
for r in rut[::-1]:
    S+=int(r)*M
    M+=1
    if M==8:
        M=2
R= S%11
RF=11-R
if RF==11:
    RF=0
if RF==10:
    RF=("k")
else:
    RF=RF
    
print ("dv=",RF)