def jerigonzo(string):
    string = string.lower()
    letras = ["a","e","i","o","u"]
    for i in letras:
        string = string.replace(i, i+"p"+i)    
    return string

if __name__ == "__main__":
    string = input("Ingrese una palabra: ")
    print(jerigonzo(string))