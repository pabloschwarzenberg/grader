def jerigonzo(string):
    string_l=list(string)
    for n in range(0,len(string_l)):
        if string_l[n]=="a":
            string_l[n]="apa"
        elif string_l[n]=="e":
            string_l[n]="epe"
        elif string_l[n]=="i":
            string_l[n]="ipi"
        elif string_l[n]=="o":
            string_l[n]="opo"
        elif string_l[n]=="u":
            string_l[n]="upu"
    listo=''.join(string_l)
    return listo