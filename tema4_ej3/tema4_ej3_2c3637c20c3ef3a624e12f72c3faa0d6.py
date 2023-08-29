#Soy Oscar Páez
def jerigonzo(string):
    traducida = ""
    for vocal in string:
        traducida += vocal
        if vocal.lower() in "aeiou":
            traducida += "p" + vocal
    return traducida
if __name__ == "__main__":
    string = input("Escribe una palabra: ")
    traducida = jerigonzo(string)

    print(traducida)
    jerigonzo(string)
    