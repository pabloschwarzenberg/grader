def sopaletras(nombre_archivo, palabras):
    with open(nombre_archivo, "r") as f:
        lineas = f.read().split('\n')

        sopa = []
        for linea in lineas:
            sopa.append(linea.split(' '))
        
        dirs = [["derecha", 0, 1], ["abajo", 1, 0], ["diagonal", 1, 1]]
        res = []

        rows = len(sopa)
        cols = len(sopa[0])

        for palabra in palabras:
            for dir in dirs:
                for row in range(rows):
                    for col in range(cols):
                        if palabra[0].upper() == sopa[row][col]:
                            f_row = row + (len(palabra) - 1) * dir[1]
                            f_col = col + (len(palabra) - 1) * dir[2]

                            done = True
                            if f_row < rows and f_col < cols:
                                for i in range(len(palabra)):
                                    if sopa[row + i * dir[1]][col + i * dir[2]] != palabra[i].upper():
                                        done = False
                                        break
                                if done:
                                    res.append((palabra, [row, col], dir[0]))

    return res

print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))