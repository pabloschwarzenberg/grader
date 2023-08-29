def rot13(palabra):
    import string
    a_l = list(palabra)
    s_l = list(string.ascii_lowercase)
    t_l = list (palabra)
    for i in range(len(a_l)):
        for j in range(len(s_l)):
            if a_l[i] == s_l[j] and j < 13:
                t_l[i] = s_l[j + 13]

            if a_l[i] == s_l[j] and j >= 13:
                t_l[i] = s_l[j - 13]
    a = "".join(t_l)
    return a

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)



