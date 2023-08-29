def rot13(palabra):
    x = 'abcdefghijklm'
    y = 'nopqrstuvwxyz'
    z=dict(zip(x + y, y + x))
    return ''.join(z.get(x.lower(), x) for x in palabra)
    pass
           