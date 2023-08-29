def mcm(a,b,c):
    if b==0:
        return c/a
    else:
        return mcm(b,a%b,c)

if __name__ == "__main__":
    print(mcm(44,88,44*88))