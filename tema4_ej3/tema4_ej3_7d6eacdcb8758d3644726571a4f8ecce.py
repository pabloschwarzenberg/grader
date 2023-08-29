def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']
    string = list(string)
    a = string.count('a')
    b = string.count('e')
    c = string.count('i')
    d = string.count('o')
    e = string.count('u')
    tot = a + b + c + d + e
    i = 0
    while i < len(string):
        if string[i] == "a":
            string.insert(i+1,'p')
            string.insert(i+2,'a')
            i +=2
            i +=1
        elif string[i] == "e":
            string.insert(i+1,'p')
            string.insert(i+2,'e')
            i +=2
            i +=1
        elif string[i] == "i":
            string.insert(i+1,'p')
            string.insert(i+2,'i')
            i +=2
            i +=1
        elif string[i] == "o":
            string.insert(i+1,'p')
            string.insert(i+2,'o')
            i +=2
            i +=1
        elif string[i] == "u":
            string.insert(i+1,'p')
            string.insert(i+2,'u')
            i +=2
            i +=1
        i +=1
    jerijeri = "".join(string)
    return(jerijeri)

if __name__ == "__main__":
    p = input("ingrese una palabra: ")
    p.lower()
    k = jerigonzo(p)
    print(k)
         