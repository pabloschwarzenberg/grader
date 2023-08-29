def rot13(palabra):
    CLEAR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    ROT13 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    TABLE = {x: y for x, y in Zip(CLEAR, ROT13)}

    for c in clear:
        yield TABLE.get(c, c)

