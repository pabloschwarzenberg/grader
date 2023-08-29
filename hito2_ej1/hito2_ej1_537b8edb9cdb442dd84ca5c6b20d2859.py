secuencia1=input("secuencia1:")
secuencia2=input("secuencia2:")

if len(secuencia1)<len(secuencia2):
    alineamiento=""
    i=1
    k=1
    while k<len(secuencia2)-1:
        a=secuencia1[i]
        b=secuencia2[k]
        if a=="A":
            if b=="A":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
        if a=="T":
            if b=="T":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
        if a=="G":
            if b=="G":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1        
        if a=="C":
            if b=="C":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
    if k==len(secuencia2)-1:
        while i<len(secuencia1)-1:
            c=secuencia1[i]
            alineamiento=alineamiento+c
            i=i+1
    if i==len(secuencia1):
        print(alineamiento)
    
if len(secuencia1)>len(secuencia2):
    alineamiento=""
    i=1
    k=1
    while k<len(secuencia1)-1:
        b=secuencia2[i]
        a=secuencia1[k]
        if a=="A":
            if b=="A":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
        if a=="T":
            if b=="T":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
        if a=="G":
            if b=="G":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1        
        if a=="C":
            if b=="C":
                alineamiento=alineamiento+b
                i=i+1
                k=k+1
            else:
                alineamiento=alineamiento+"_"
                k=k+1
    if k==len(secuencia1)-1:
        while i<len(secuencia2)-1:
            c=secuencia2[i]
            if c=="A":
                alineamiento=alineamiento+"A"
            if c=="T":
                alineamiento=alineamiento+"T"
            if c=="C":
                alineamiento=alineamiento+"C"
            if c=="G":
                alineamiento=alineamiento+"G"
            i=i+1
        print(alineamiento)    