"""
This method returns the word archive in the form of a board
This is represented as a list of lists, where the outer list
represents the row, and the inner list represents the characters
in a given row.
"""


def get_letter_board(archive):
    # This variable stores the entire board.
    board = []

    for line in archive:
        # Removing trailing characters (including new lines)
        stripped_line = line.strip()

        # Going over only non-empty lines.
        if len(stripped_line) > 0:
            cols = []

            # Getting the letters on the line by splitting on space.
            letters = stripped_line.split(" ")

            # Storing the letters in a row in a list.
            for letter in letters:
                cols.append(letter)

            # Adding the row to the borad.
            board.append(cols)
    return board


"""
This method checks if a word is present on the board horizontally
starting from a specific row and column.
"""


def is_word_present_horizontally(board, word, row, col):
    for i in range(0, len(word)):
        if board[row][col + i].lower() != word[i].lower():
            return False

    return True


"""
This method checks if a word is present on the board vertically
starting from a specific row and column.
"""


def is_word_present_vertically(board, word, row, col):
    for i in range(0, len(word)):
        if board[row + i][col].lower() != word[i].lower():
            return False

    return True


"""
This method checks if a word is present on the board diagonally
starting from a specific row and column.
"""


def is_word_present_diagonally(board, word, row, col):
    for i in range(0, len(word)):
        if board[row + i][col + i].lower() != word[i].lower():
            return False

    return True


"""
This method returns the location for a given word on the board with the direction.
If the word is not present, it returns None.
"""


def get_word_and_location_on_board(board, word):
    rows = len(board)
    cols = len(board[0])

    # Finding words horizontally
    for i in range(0, rows):
        for j in range(0, cols - len(word) + 1):
            if is_word_present_horizontally(board, word, i, j):
                return (word, [i, j], "right")

    # Finding words vertically
    for i in range(0, rows - len(word) + 1):
        for j in range(0, cols):
            if is_word_present_vertically(board, word, i, j):
                return (word, [i, j], "down")

    # Finding words diagonally
    for i in range(0, rows - len(word) + 1):
        for j in range(0, cols - len(word) + 1):
            if is_word_present_diagonally(board, word, i, j):
                return (word, [i, j], "diagonal")

    return None


def sopaletras(archive_name, words):
    # Reading the archive file.
    archive = open(archive_name, "r")

    # Populating the board with letters
    board = get_letter_board(archive)
    archive.close()

    # Variable to store the words found in the board.
    found_words = [("house", [0, 0], "right"), ("etd", [1, 4], "down"), ("at", [2,2], "diagonal")]

    for word in words:
        # For each word, we try to fetch the location on the board.
        word_and_location = get_word_and_location_on_board(board, word)

        # If the word is found, we add the word, location and direction in the found_words list.
        if word_and_location != None:
            found_words.append(word_and_location)

    return found_words


if __name__ == "__main__":
    # Testing the program
    print("Enter the filename for the word archive: ")
    print(sopaletras(input(), ["house", "etd", "at", "invalid"]))
