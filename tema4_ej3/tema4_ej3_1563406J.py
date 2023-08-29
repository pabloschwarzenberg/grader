def jerigonzo(string):
    r="a,e,i,o,u"
    r.split(",")
    x=0
    for c in string:
        for i in range(0,9):
            if r[i].find(c)!=-1:
                string=string[:x+1]+"p"+r[i]+string[x+1:]
                x=x+2
        x=x+1
    return string
if __name__ == "__main__":
    string=input("Ingrese texto aqui : ")
    print(jerigonzo(string))
         