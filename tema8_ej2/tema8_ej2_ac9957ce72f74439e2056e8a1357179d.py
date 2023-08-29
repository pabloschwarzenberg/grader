def buscarTodas(a,b):
    _letter_positions = ""

    for i in range(len(a)):
        if a[i: i + len(b)] == b:
            _letter_positions += str(i) + ' '
    return _letter_positions[:-1]

if __name__ == "__main__":
    pass
           