def jerigonzo(string):
    string_l=list(string)
    for i in range(0,len(string_l)):
        if string_l[i]=="a":
            string_l[i]="apa"
            continue
        if string_l[i]=="e":
            string_l[i]="epe"
            continue
        if string_l[i]=="i":
            string_l[i]="ipi"
            continue
        if string_l[i]=="o":
            string_l[i]="opo"
            continue
        if string_l[i]=="u":
            string_l[i]="upu"
            continue
    string="".join(string_l)    
    return string

if __name__ == "__main__":
    string=input("Ingrese palabra:")
    print(jerigonzo(string))
