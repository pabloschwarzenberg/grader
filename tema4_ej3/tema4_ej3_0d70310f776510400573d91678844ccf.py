def jerigonzo(string):
    string= [""]
    vocal  = ["a","e","i","o","u"]
    for i in range (1,len(string)):
        string.index(i)
        if i == vocal[i]:
            i = i + "p" + i
            string.append(i)

    return string

if __name__ == "__main__":
    pass
         