def jerigonzo(string):

    string=string.lower()

    Pjerigonzo = ""

    for i in string:

        if i == "a":

            Pjerigonzo += "apa"

        elif i == "e":

            Pjerigonzo += "epe"

        elif i == "i":

            Pjerigonzo += "ipi"

        elif i == "o":

            Pjerigonzo += "opo"

        elif i == "u":

            Pjerigonzo += "upu"

        else:

            Pjerigonzo += i


    return Pjerigonzo

if __name__ == "__main__":
    pass
         