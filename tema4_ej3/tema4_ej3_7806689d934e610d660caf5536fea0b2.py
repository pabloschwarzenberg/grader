def jerigonzo(n):
    n=list(n)
    i=0
    a=len(n)
    while a>0:
        if n[i]=="a":
                n[i]="apa"
        elif n[i]=="e":
                n[i]="epe"
        elif n[i]=="i":
                n[i]="ipi"
        elif n[i]=="o":
                n[i]="opo"
        elif n[i]=="u":
                n[i]="upu"
        i=i+1
        a=a-1
    return("".join(n))


if __name__ == "__main__":
    n=input("ingrese la palabra: ")
    print(jerigonzo(n))
    
         