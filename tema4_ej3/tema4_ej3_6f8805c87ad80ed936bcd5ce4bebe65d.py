def jerigonzo(string):
    string= string.replace("a","apa")
    string= string.replace("e","epe")
    string= string.replace("i","ipi")
    string= string.replace("o","opo")
    string= string.replace("u","upu")
    print(string)
    return string

if __name__ == "__main__":
    string= str(input("Ingrese palabra: "))
    jerigonzo(string)
        