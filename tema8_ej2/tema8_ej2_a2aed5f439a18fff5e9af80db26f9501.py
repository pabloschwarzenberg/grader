def buscarTodas(a, b):
    a_l=list(a)
    for i in range(len(a)):
        if a_l[i] == b:
            a_l[i] = str(i)

        else:
            a_l[i] = " "
            while a_l[i] == a_l[i - 1]:
                i = i - 1
                a_l[i] = ""
            for j in range(len(a)-1, len(a)):
                if a_l[j]==" ":
                    a_l[j]=""

    a = "".join(a_l)
    return a

if __name__ == "__main__":
    a = str(input())
    b = str(input())
    print(buscarTodas(a, b))
