def binario(n, binary=None):
    if binary is None:
        binary = ''
    if n > 0:
        binario(n - 1, binary + '0')
        binario(n - 1, binary + '1')
    else:
        print(binary)
n=int(input())
binario(n)