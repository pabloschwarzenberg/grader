def buscarTodas(a, b):
    resultado = ""
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            resultado += str(i) + " "
    return resultado.rstrip()

if __name__ == "__main__":
    a = "tres tristes tigres"
    b = "t"
    indices = buscarTodas(a, b)
    print(indices)  # 0 5 9 13
           