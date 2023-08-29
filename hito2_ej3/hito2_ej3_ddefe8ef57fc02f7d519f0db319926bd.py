def subsec(s,n):
    subsecs = []
    substrings = []
    for i in range(len(s) - n + 1):
        subsecs.append(s[i:i + n])
    for i in subsecs:
        if subsecs.count(i) == 1:
            substrings.append(i)
    if len(substrings) == 0:
        substrings.append("ninguna")
    return substrings
string = input()
n = int(input())
substrings = subsec(string,n)
for i in substrings:
    print(i)