def jerigonzo(string):
    string=str(string)
    s=""
    for i in string:
        if i=="a":
            s+="apa"
        elif i=="e":
            s+="epe"
        elif i=="i":
            s+="ipi"
        elif i=="o":
            s+="opo"
        elif i=="u":
            s+="upu"
        
        else:
            s+=i
    return s
    
         