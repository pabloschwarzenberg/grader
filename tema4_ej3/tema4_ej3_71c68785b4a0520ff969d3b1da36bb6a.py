def jerigonzo(string):
    textrad = ""

    for letra in string:
        if letra.lower() in "aeiou":
            textrad += letra + "p" + letra.lower()
        else:
            textrad += letra

    return textrad

    if __name__ == "_main_":
      main()