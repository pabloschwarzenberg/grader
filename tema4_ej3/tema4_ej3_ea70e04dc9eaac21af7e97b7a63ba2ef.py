def jerigonzo(string):
    nuevaa=string.replace("a","apa")
    nuevae=nuevaa.replace("e","epe")
    nuevai=nuevae.replace("i","ipi")
    nuevao=nuevai.replace("o","opo")
    nuevau=nuevao.replace("u","upu")
    
    return nuevau

if __name__ == "__main__":
    a=input("inserte su traduccion a jerigonzo")
    b=print(jerigonzo(a))
    pass