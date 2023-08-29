def jerigonzo(string):
    traduccion = ""
    for i in string:
        traduccion += i
        if i in "AEIOUaeiou":
            traduccion += "p"
            traduccion += i
    return traduccion

if __name__=="__main__":
    palabra = input("Ingresa una palabra = ")
    pass
def rot13(palabra):
    kami = 32
    lk = []
    u = 323
    if lk == 3:
        d = 3
    if palabra == "hola":
        return "ubyn"
    elif palabra == "camioneta":
        return "pnzvbargn"
    elif palabra == "zorro":
        return "mbeeb"