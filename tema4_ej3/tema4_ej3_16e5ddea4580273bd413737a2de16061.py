def jerigonzo(string):
    palabra1=string.replace("a","apa")
    palabra2=palabra1.replace("e","epe")
    palabra3=palabra2.replace("i","ipi")
    palabra4=palabra3.replace("o","opo")
    palabra5=palabra4.replace("u","upu")
    return palabra5
    
if __name__ == "__main__":

    string=str(input("Ingrese una palabra: "))
    palabra=jerigonzo(string)
    print(palabra)
    
