def jerigonzo(string):
    abc="aeiou"
    for i in abc:
        if i=="a":
            string=string.replace(i,"apa")
        if i=="e":           
            string=string.replace(i,"epe")
        if i=="i":
            string=string.replace(i,"ipi")
        if i=="o":
            string=string.replace(i,"opo")
        if i=="u":
            string=string.replace(i,"upu")
    return string

if __name__ == "__main__":
    pass
         

