def jerigonzo(string):
    s1=""
    for i in string:
        if i == "a":
            s1 = s1 + "apa"
        elif i =="e":
            s1 = s1 + "epe"
        elif i=="i":
            s1= s1 + "ipi"
        elif i=="o":
            s1=s1 + "opo" 
        elif i=="u":
            s1= s1 + "upu"
        else:
            s1 = s1 + i
    return s1
            

if __name__ == "__main__":
    pass
         