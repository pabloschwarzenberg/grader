def jerigonzo(string):
    import random
    nustring = ""
    for pos in range(len(string)):
        yep = string[pos]
        if yep in ["a","e","i","o","u"]:
            print("ches")
            nustring = nustring + string[pos] + "p" + string[pos]
        else:
            nustring = nustring + string[pos]
    return nustring

if __name__ == "__main__":
    pass
         