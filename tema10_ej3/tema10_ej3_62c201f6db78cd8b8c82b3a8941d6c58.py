def sopaletras(file_name, words):
    # Leer la sopa de letras desde el archivo
    with open(file_name, 'r') as file:
        alphabet_soup = [list(line.strip()) for line in file]

    rows = len(alphabet_soup)
    cols = len(alphabet_soup[0])

    def check_horizontal(word):
        for row in range(rows):
            for col in range(cols - len(word) + 1):
                if ''.join(alphabet_soup[row][col:col+len(word)]) == word:
                    return [row, col], 'derecha'
        return None

    def check_vertical(word):
        for col in range(cols):
            for row in range(rows - len(word) + 1):
                if ''.join([alphabet_soup[row+i][col] for i in range(len(word))]) == word:
                    return [row, col], 'abajo'
        return None

    def check_diagonal(word):
        for row in range(rows - len(word) + 1):
            for col in range(cols - len(word) + 1):
                if ''.join([alphabet_soup[row+i][col+i] for i in range(len(word))]) == word:
                    return [row, col], 'diagonal'
        return None

    results = []
    for word in words:
        starting_pos = check_horizontal(word)
        if starting_pos:
            results.append((word, starting_pos[0], starting_pos[1]))
            continue

        starting_pos = check_vertical(word)
        if starting_pos:
            results.append((word, starting_pos[0], starting_pos[1]))
            continue

        starting_pos = check_diagonal(word)
        if starting_pos:
            results.append((word, starting_pos[0], starting_pos[1]))
            continue

    return results

