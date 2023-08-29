def jerigonzo(string):
    palabra=[]
    traduccion=''
    util=''
    for i in string:
        if (i.lower()=='a'or i.lower()=='e'or i.lower()=='i'or i.lower()=='o'or i.lower()=='u'):
            util=i+'p'+i.lower()
            palabra.append(util)
        else:
            palabra.append(i)
    for i in palabra:
        traduccion=traduccion+i
    return traduccion

if __name__ == "__main__":
    pass
         