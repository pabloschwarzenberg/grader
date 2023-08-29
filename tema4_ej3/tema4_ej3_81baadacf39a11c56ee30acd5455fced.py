def jerigonzo(string):
    string1=list(string)
    for i in range(len(string1)):
        letra=string1[i].lower()
        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            string1[i]+="p"+string1[i]
    return "".join(string1)
if __name__ == "__main__":
    string=input("Ingrese su palabra o frase: ")
    print(jerigonzo(string))        