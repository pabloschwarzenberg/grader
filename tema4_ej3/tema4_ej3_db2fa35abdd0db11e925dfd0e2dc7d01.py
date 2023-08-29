string=""
def inpt(n):
    palabra=str(input("Palabra: "))
    palabra=palabra.lower()
    palabra=list(palabra)
    return jerigonzo(palabra)
def jerigonzo(s):
    global string
    for i in s:
        if i=="a":
            i="apa"
            string=string+i
        elif i=="e":
            i="epe"
            string=string+i
        elif i=="i":
            i="ipi"
            string=string+i
        elif i=="o":
            i="opo"
            string=string+i
        elif i=="u":
            i="upu"
            string=string+i        
        else:
            string=string+i
    return string
if __name__ == "__main__":
    print(inpt(string))