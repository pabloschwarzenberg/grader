def jerigonzo(a):
    l=a.replace("a","apa")
    l1=l.replace("e","epe")
    l2=l1.replace("i","ipi")
    l3=l2.replace("o","opo")
    l4=l3.replace("u","upu")
    return l4

if __name__ == "__main__":
    texto=str(input("Ingrese el Texto a Convertir. "))
    a=texto.lower()

    print(jerigonzo(a))
         