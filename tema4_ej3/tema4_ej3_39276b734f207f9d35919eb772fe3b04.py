def jerigonzo(result):
    P_Jeringoso = ""
    for l in result:
        if l in "aeiouAEIOU":
            P_Jeringoso += l
            P_Jeringoso += "p"
        P_Jeringoso += l
    return P_Jeringoso
#if __name__ == "__main__":
    #pass
print(jerigonzo("bienvenidos a mi clase"))
         