def jerigonzo(string):

    a=len(string)
    i=0


    j=[]
    while(i<a):



        if(string[i]=="a") or (string[i]=="e") or (string[i]=="i") or (string[i]=="o") or (string[i]=="u"):
            print(string[i])
            j.append(string[i])
            j.append("p")
            j.append(string[i])

        else:
            print(string[i])
            j.append(string[i])
        i=i+1
    string="".join(j)
    return string
         