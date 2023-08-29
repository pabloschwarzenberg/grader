def sopaletras(nombre_archivo, palabras):
    count = 0
    final = []
    archivo = open(nombre_archivo, "r")
    rows = archivo.readlines()
    archivo.close()
    for x in rows:
        x = x.replace(" ", "").strip()
        rows[count] = x.lower()
        count += 1

    for x in palabras: # for each word, search for every occurrence of it's initial letter
        count = 0
        posib = []
        for y in rows:
            count = 0
            while count < len(y):
                if x[0] == y[count]:
                    posib.append([count, rows.index(y)]) # (coordinates x, y)
                count += 1

        for z in posib: # check for word directions
            try:
                if rows[z[1]][z[0]+1] == x[1]: # word might be horizontal
                    correct = True
                    count2 = z[0]
                    for i in x:
                        if rows[z[0]][count2] == i:
                            correct = True
                        else:
                            correct = False
                        count2 += 1
                    if correct:
                        final.append((x, [z[1], z[0]], "derecha"))
                if rows[z[1]+1][z[0]] == x[1]: # word might be vertical
                    correct = True
                    count2 = z[1]
                    for i in x:
                        if rows[count2][z[0]] == i:
                            correct = True
                        else:
                            correct = False
                        count2 += 1
                    if correct:
                        final.append((x, [z[1], z[0]], "abajo"))
                if rows[z[1]+1][z[0]+1] == x[1]: # word might diagonal
                    correct = True
                    count2 = [z[1], z[0]]
                    for i in x:
                        if rows[count2[0]][count2[1]] == i:
                            correct = True
                        else:
                            correct = False
                        count2[0] += 1
                        count2[1] += 1
                    if correct:
                        final.append((x, [z[1], z[0]], "diagonal"))
            except IndexError:
                pass
    return final


if __name__ == "__main__":
    #print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    #print(sopaletras("sopa.txt", ["casa"]))
    #print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))