def jerigonzo(a):
    b=a
    b=b.replace("a","apa")
    b=b.replace("e","epe")
    b=b.replace("i","ipi")
    b=b.replace("o","opo")
    b=b.replace("u","upu")
    return b

if __name__=="__main__":
    m=str(input("ingrese una palabra"))
    print(jerigonzo(m))