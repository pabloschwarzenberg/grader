def jerigonzo(string):
    string2=list(string)
    vocal=["a","e","i","o","u"]
    string3=[]
    for i in string2:
        if i in vocal:
            i=i+"p"+i
        string3+=i
    string3="".join(string3)
    return string3

if __name__ == "__main__":
    pass
         