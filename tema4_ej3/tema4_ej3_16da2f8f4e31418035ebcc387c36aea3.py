def jerigonzo(string):
    if string.find("a")!=-1:
        string=string.replace("a","apa")
    else:
        pass
    if string.find("e")!=-1:
        string=string.replace("e","epe")
    else:
        pass
    if string.find("i")!=-1:
        string=string.replace("i","ipi")
    else:
        pass
    if string.find("o")!=-1:
        string=string.replace("o","opo")
    else:
        pass
    if string.find("u")!=-1:
        string=string.replace("u","upu")
    else:
        pass
    return string

if __name__ == "__main__":
    print(jerigonzo("paralelepipedo"))
         