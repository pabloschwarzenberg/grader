def jerigonzo(string):
    l = list(string)
    i = 0
    while i <= (len(l)-1):
        if l[i] == "a" or l[i] == "e" or l[i] == "i" or l[i] == "o" or l[i] == "u":
            l.insert((i+1), ("p" + l[i]))
            i += 1
        else:
            i += 1
    l = ''.join(l)

    return l