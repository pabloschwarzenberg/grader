def jerigonzo(string):
    ocultar=list(string)
    i=0
    while i<len(ocultar):
        if ocultar[i]=="a":
            ocultar[i]="apa"
            i=i+1
        elif ocultar[i]=="e":
            ocultar[i]="epe"
            i=i+1
        elif ocultar[i]=="i":
            ocultar[i]="ipi"
            i=i+1
        elif ocultar[i]=="o":
            ocultar[i]="opo"
            i=i+1
        elif ocultar[i]=="u":
            ocultar[i]="upu"
            i=i+1
        else:
            i=i+1
    nueva="".join(ocultar)
    return nueva

if __name__ == "__main__":
    pass
         