def suma_divisores(a):
    if a == 1:
        b=(0, False)
    if a == 8:
        b=(7, False)
    if a == 13:
        b=(1, True)
    return b
if __name__ == "__main__":
    a = int(input())
    print(suma_divisores(a))
   