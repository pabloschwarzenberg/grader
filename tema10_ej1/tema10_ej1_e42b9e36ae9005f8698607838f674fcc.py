def mcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return mcd(b, r)


def mcm(a, b, ab):
    return int(ab / mcd(a, b))


if __name__ == '__main__':
    print(str(mcm(88, 44, 88*44)))
