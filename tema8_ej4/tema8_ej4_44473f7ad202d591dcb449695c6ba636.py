def rot13(palabra):
    mover = ""
    abcdario = "abcdefghijklmnopqrstuvwxyz"
    for i in palabra:
        mover += abcdario[(abcdario.find(i) + 13) % 26]
    return mover




