def jerigonzo(string):
    string=list(string)
    i=0
    while i<len(string):
        if string[i]=="a":
            string.insert(i+1,"pa")
            i=i+3
        elif string[i]=="e":
            string.insert(i+1,"pe")
            i=i+3
        elif string[i]=="i":
            string.insert(i+1,"pi")
            i=i+3
        elif string[i]=="o":
            string.insert(i+1,"po")
            i=i+3
        elif string[i]=="u":
            string.insert(i+1,"pu")
            i=i+3
        else:
            i=i+1
    string="".join(string)
    return string

if __name__ == "__main__":
    string=input("String: ")
    print(jerigonzo(string))

         