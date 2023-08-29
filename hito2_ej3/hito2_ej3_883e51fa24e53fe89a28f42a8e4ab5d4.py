   def print_substrings(s, n):
    substrings = []
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if substring not in substrings and s.count(substring) == 1:
            substrings.append(substring)
    if len(substrings) == 0:
        print("ninguna")
    else:
        for substring in substrings:
            print(substring)   