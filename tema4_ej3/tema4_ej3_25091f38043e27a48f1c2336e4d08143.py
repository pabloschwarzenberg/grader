def jerigonzo(string):
    l=list(string)
    i=0
    while i<(len(l)):
        if l[i]=="a":
            l[i]="apa"
            i+=1
        elif l[i]=="e":
            l[i]="epe"
            i+=1
        elif l[i]=="i":
            l[i]="ipi"
            i+=1
        elif l[i]=="o":
            l[i]="opo"
            i+=1
        elif l[i]=="u":
            l[i]="upu"
            i+=1
        else:
            i+=1
    b="".join(l)
    return (b)
