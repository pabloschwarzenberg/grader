def buscarTodas(a, b):
    ubicacion = []

    for i in range(len(a) - len(b)):
        if a[i: i + len(b)] == b:
            ubicacion.append(str(i))

    return ' '.join(ubicacion)


if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres', 't'))
