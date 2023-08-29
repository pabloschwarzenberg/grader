def buscarTodas(a, b):
    indices = ""
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            indices += str(i) + " "
    return indices[:-1]

if __name__ == "__main__":
    a = input("Ingrese el string a: ")
    b = input("Ingrese el string b: ")
    print(buscarTodas(a, b))