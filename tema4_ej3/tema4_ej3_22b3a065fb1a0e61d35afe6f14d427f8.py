def jerigonzo(string):
    traduccion = ""
    for i in string:
        if i in "AEIOUaeiou":
            traduccion += i
            traduccion += "p"
        traduccion += i
    string = traduccion    
    
    return string
if __name__ == "__main__":
    string = str(input("ingresa una palabra: "))
    pass
         