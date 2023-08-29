def jerigonzo(string):
    string=string.lower()
    string=list(string)
    vocales=["a","e","i","o","u"]
    i=0
    while i<len(string):
        if string[i] in vocales:
            string.insert(i+1,"p")
            string.insert(i+2,string[i])
            i+=3
        else:
            i+=1
    string=''.join(string)       
    return string

if __name__ == "__main__":
    pass
         