def jerigonzo(p):
    p=list(p)
    i=0
    while i<len(p):
        if p[i]=="a":
            p[i]="apa"
        if p[i]=="e":
            p[i]="epe"
        if p[i]=="i":
            p[i]="ipi"
        if p[i]=="o":
            p[i]="opo"
        if p[i]=="u":
            p[i]="upu"
        i=i+1
    p="".join(p)
    return p

if __name__ == "__main__":
    pass
         