def sopaletras(nombre_archivo, palabras):
    archivo = open(nombre_archivo, "r")

    results_list = []

    grid = []

    for line in archivo:
        grid.append(line.replace(" ", "").replace("\n", ""))

    for y, item in enumerate(grid):
        for x, char in enumerate(item):
            # print(x, y)
            for palabra in palabras:
                if char.lower() == palabra[0].lower():

                    if grid[y][x:len(palabra)].lower() == palabra.lower():
                        results_list.append((palabra, [y, x], "derecha"))

                    palabra_abajo = ""
                    palabra_diagonal = ""

                    for i in range(len(palabra)):
                        try:
                            palabra_abajo += grid[y + i][x]
                            palabra_diagonal += grid[y + i][x + i]
                        except IndexError:
                            break

                    if palabra_diagonal.lower() == palabra.lower():
                        results_list.append((palabra, [y, x], "diagonal"))

                    elif palabra_abajo.lower() == palabra.lower():
                        results_list.append((palabra, [y, x], "abajo"))

    archivo.close()

    return results_list

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           