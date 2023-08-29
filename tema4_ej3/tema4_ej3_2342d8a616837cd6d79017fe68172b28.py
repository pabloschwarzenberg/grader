def jerigonzo(string):
    string_l=list(string)
    jerigonzo=""
    jerigonzo_l=list(jerigonzo)
    for n in string_l:
        if n=="a":
            n="apa"
        elif n=="e":
            n="epe"
        elif n=="i":
            n=="ipi"
        elif n=="o":
            n="opo"
        elif n=="u":
            n="upu"
        else:
            n=n
        jerigonzo_l.append(n)
        jerigonzo="".join(jerigonzo_l)
    return jerigonzo
print(jerigonzo)

if __name__ == "__main__":
    pass
         