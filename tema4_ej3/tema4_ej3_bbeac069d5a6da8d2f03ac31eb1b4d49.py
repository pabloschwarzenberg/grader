def jerigonzo(string):
    string = string.lower()
    string = list(string)
    i = 0
    while i < len(string):
        if string[i] in ["a","e","i","o","u"]:
            string[i] = string[i] + "p" + string[i]
            i += 1
        else:
            i += 1
    string = "".join(string)
    return string