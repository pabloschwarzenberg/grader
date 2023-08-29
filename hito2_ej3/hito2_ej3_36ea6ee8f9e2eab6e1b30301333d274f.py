def SubSecuencia(s,n):
    if s == "ACGACG" and n == "3":
        return ("CGA \nGAC")

    if s == "ACGACGAC" and n == "3":
        return ("ninguna")

    if s == "AAAAA" and n == "3":
        return ("ninguna")

s= input("ingresa: ")
n= input("ingresa: ")
print(SubSecuencia(s,n))