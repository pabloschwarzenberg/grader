def jerigonzo(string):
    L = list(string)
    for i in range(len(string)):
        if L[i] in "aeiouAEIOU":
            L[i] = L[i] + "p" + L[i]
    string = "".join(L)
    return string

         