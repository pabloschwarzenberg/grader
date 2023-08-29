trad=""
string=""
def jerigonzo(string):
        trad = str("")
        for letra in string:
               if letra in "AEIOUaeiou":
                   trad += letra
                   trad +="p"
               trad += letra
        print(trad)

        return trad
if __name__ == "__main__":
    string = input("")
jerigonzo(string)
print(trad)