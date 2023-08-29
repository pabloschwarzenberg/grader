def buscarTodas(a, b):
    return " ".join(str(i) for i in range(len(a)) if a[i:i+len(b)] == b)

if __name__ == "__main__":
    a = "tres tristes tigres"
    b = "t"
    print(buscarTodas(a, b))