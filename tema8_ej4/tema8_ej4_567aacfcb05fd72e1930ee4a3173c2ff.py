def rot13(palabra):
    orig = 'abcdefghijklm'
    tgt = 'nopqrstuvwxyz'
    rotmapper = dict(zip(orig + tgt, tgt + orig))
    return ''.join(rotmapper.get(x.lower(), x) for x in palabra)

if __name__ == "__main__": 
    main()