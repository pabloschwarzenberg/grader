vocales = ["a","e","i","o","u"]
def jerigonzo(string):
    a = list(string)
    string_n = []
    for i in a:
        string_n.append(i)
        if i in vocales:
            string_n.append("p")
            string_n.append(i)
    string_n = str("".join(string_n))
    return string_n

if __name__ == "__main__":
    pass
         