def jerigonzo(string):
    string = list(string)
    new_string=[]
    for i in string:
        if i in "AEIOUaeiou":
            new_string.append(i+"p"+i.lower())
            continue
        new_string.append(i)
    return "".join(new_string)
         