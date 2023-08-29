def buscarTodas(a, b):
    haystack = a
    needle = b
    c = ''
    count = 0
    for i, _ in enumerate(haystack):
        if haystack[i:i + len(needle)] == needle:
            count += 1
            if count<2:
                c += ("" + str(i))
            else:
                c += (" " + str(i))
    return c

if __name__ == "__main__":
    pass
print(buscarTodas('como estamos','o'))