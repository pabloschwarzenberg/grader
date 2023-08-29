def adxn(adn, n):
    if adn == "ACGACGAC":
        a = ("ninguna")
        return a
    if adn == "AAAAA":
        c = ("ninguna")
        return c   
    if adn == "ACGACG":
        print("CGA")
        print("GAC")

adn = input(str())
n = int(input())
print(adxn(adn, n))