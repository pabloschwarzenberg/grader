def jerigonzo(string):
    string_list=[]
    aeiou=["a","e","i","o","u"]
    for i in string:
        string_list.append(i)
        if i in aeiou:
            string_list.append("p")
            string_list.append(i)
    string="".join(str(x) for x in string_list)
        
    return string






if __name__ == "__main__":
    string=input("Que quieres traducir:")
    print(jerigonzo(string))
    pass