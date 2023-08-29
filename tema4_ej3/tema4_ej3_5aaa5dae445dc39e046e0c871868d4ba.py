def jerigonzo(string):
    count = 0
    original = [x for x in string]
    string = [x for x in string]
    counts = [0, 0, 0, 0, 0]
    vowels = ["a", "e", "i", "o", "u"]
    for x in original:
        if x in vowels:
            counts[vowels.index(x)] += 1
            string.insert(count + 1, "p")
            string.insert(count + 2, x)
            count += 2
        count += 1
    return "".join(string)