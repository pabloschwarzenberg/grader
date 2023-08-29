def jerigonzo(string):
    traducida = ""
    for x in string:
        traducida += x
        if x.lower() in "aeiou":
            traducida += "p" + x
    return traducida

if __name__ == "__main__":
    jerigonzo()
   