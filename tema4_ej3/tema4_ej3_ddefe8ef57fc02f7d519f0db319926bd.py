def jerigonzo(string):
    for i in ["a", "e", "i","o","u"]:
        string = string.replace(i, i + "p" + i)
    return string

         