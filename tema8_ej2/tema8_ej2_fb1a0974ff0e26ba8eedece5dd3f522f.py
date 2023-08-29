def buscarTodas(a,b):
    string = ""
    for i in range(len(a)):
        if a[i] == b:
            j = str(i)
            string = string + j + " "
    return string.strip()

if __name__ == "__main__":
    pass
               
