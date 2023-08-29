def find_unique_substrings(s, n):
    unique_subs = set()
    repeated_subs = set()    
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if sub in unique_subs:
            repeated_subs.add(sub)
        else:
            unique_subs.add(sub)
    unique_subs = unique_subs - repeated_subs
    if len(unique_subs) == 0:
        print("ninguna")
    else:
        for sub in unique_subs:
            print(sub)
s = input("Introduce el string: ")
n = int(input("Introduce el valor de n: "))
find_unique_substrings(s, n)

      