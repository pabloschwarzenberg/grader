 def unique_substrings(s, n):
    unique_subs = []
    for i in range(len(s)-n+1):
        sub = s[i:i+n]
        if s.count(sub) == 1 and sub not in unique_subs:
            unique_subs.append(sub)
    if len(unique_subs) == 0:
        print("ninguna")
    else:
        for sub in unique_subs:
            print(sub)

unique_substrings("ACGACG", 3)
unique_substrings("ACGACGAC", 3)
unique_substrings("AAAAA", 3)     