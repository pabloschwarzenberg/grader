def mcm(a, b, m):
    if a == 0:
        x = m/b
        return x
    if b == 0:
        x = m/a
        return x
    if a > b and a != 0 and b != 0:
        return mcm(b, a % b, m)
    if b > a != 0 and b != 0:
        return mcm(a, b % a, m)

if __name__=="__main__":
    pass
           