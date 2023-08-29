def jerigonzo(n):
     n=n.replace("a","apa")
     n=n.replace("e","epe")
     n=n.replace("i","ipi")
     n=n.replace("o","opo")
     n=n.replace("u","upu")
     return n


if __name__ == "__main__":
    print("Bienvenido al Jerigonzo")
    print("Piensa en una palabra para transformarla.")
    j=str(input("Ingrese una palabra: "))
    print(jerigonzo(j))
    pass
         


