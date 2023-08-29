def jerigonzo(string):
    s=list(string)
    for i in range(0,len(s)):
        if(s[i]=="a"):           
            s[i]="apa"
        if(s[i]=="e"):
            s[i]="epe"
        if(s[i]=="i"):
            s[i]="ipi"
        if(s[i]=="o"):
            s[i]="opo"
        if(s[i]=="u"):
            s[i]="upu"
    string="".join(s)
    return string

if __name__ == "__main__":
    string=input("palabra:")
    print(jerigonzo(string))
