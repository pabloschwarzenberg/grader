def jerigonzo(string):
    j1=list(string)
    list1=["a", "e", "i","o","u"]
    for i in range(len(j1)):
        for j in range(len(list)):
            if(j1[i]==list1[j]):
                j1[i]=list1[j]+"p"+list1[j]
    div=""
    for h in range(len(j1)):
        div=div+j1[h]
        string=div
        return string