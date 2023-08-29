def jerigonzo(string):
    pa = ""
    vo = ["a","e","i","o","u"]
    for i in string:
        if i in vo:
            pa += i
            pa += "p"
            pa += i
        else:
            pa += i
    return pa
         