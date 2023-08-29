def jerigonzo(string):
    if "a" in string:
        string=string.replace("a","apa")
    if "e" in string:
        string=string.replace("e","epe")
    if "i" in string:
        string=string.replace("i","ipi")
    if "o" in string:
        string=string.replace("o","opo")
    if "u" in string:
        string=string.replace("u","upu")
    return string

if __name__ == "__main__":
    palabra=input("Ingrese palabra: ")
    p2=jerigonzo(palabra)
    print(p2)
