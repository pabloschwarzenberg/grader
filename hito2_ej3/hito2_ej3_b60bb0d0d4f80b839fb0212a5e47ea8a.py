sec=input("secuencia:")
N=int(input("largo de secuencia:"))
i=0
lar=len(sec)
fin=0
C=2
val=lar%N
S1=0
while fin<lar and val==0:
    fin=N+i
    S=sec[i:fin]
    i=i+1
    REV=sec.count(S)
    if REV==1 and S1!=S:
        S1=S
        print(S1)
        C=1
if C==2 or val==1:
    print("ninguna")

    
        
