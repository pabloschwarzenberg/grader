def buscarTodas(a, b):
    indices = [str(i) for i, c in enumerate(a) if c == b]
    return ' '.join(indices)
if __name__ == "__main__":
    resultado = buscarTodas('tres tristes tigres', 't')
    print(resultado)

           