def buscarTodas(a, b):
    result = [str(i) for i in range(len(a)) if a.startswith(b, i)]
    return " ".join(result)


if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres', 't'))
