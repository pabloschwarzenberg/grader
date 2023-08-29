def jerigonzo(string):
    r=list(string)
    for i in range(len(r)):
        if r[i]=="a":
            r[i]="apa"
        elif r[i]=="e":
            r[i]="epe"
        elif r[i]=="i":
            r[i]="ipi"
        elif r[i]=="o":
            r[i]="opo"
        elif r[i]=="u":
            r[i]="upu"
    return "".join(r)
if __name__=="__main__":
    string=str(input("Ingrese la palabra: "))
    print("Traducción: ",jerigonzo(string))

         