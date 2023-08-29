#PRIMO O NO
def PRIMO(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for m in range(2, num):
            if num % m == 0:
                return False
        return True
for m in range(1, 300):
    print(m, PRIMO(m))         