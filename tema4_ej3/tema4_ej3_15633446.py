def traductor (string):
    jerigonzo=""
    for i in range(0,len(string)):
        if(string[i]=="a")or(string[i]=="e")or(string[i]=="i")or(string[i]=="o")or (string[i]=="u"):
            jerigonzo += string[i]+"p"+string[i]
        else:
            jerigonzo += string[i]
    return jerigonzo
   
if __name__ == "__main__":
    pass
         