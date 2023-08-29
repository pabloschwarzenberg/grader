def jerigonzo(string):
    i = 0
    a = 0
    frasef = ""
    a = string.count("a")
    e = string.count("e")
    i = string.count("i")
    o = string.count("o")
    u = string.count("u")
    x = len(string) + (a + e + i + o + u) * 2
    z = len(string)
   
    while x>0:
        if string[0] == "a" or string[0] == "e" or string[0] == "i" or string[0] == "o" or string[0] == "u":
            frasef += string[0] + "p" + string[0]
            string = string[1:]
        else:
            frasef+=string[0]
            string = string[1:]

        if len(frasef) == x:
            break

    return frasef
      
if __name__ == "__main__":
    pass
         