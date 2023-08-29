def o_substrings_u(sec, n):
    substrings = []
    count = {}
    
    for i in range(len(sec) - n + 1):
        substring = sec[i:i+n]
        if substring in count:
            count[substring] += 1
        else:
            count[substring] = 1

    for substring in count:
        if count[substring] == 1:
            substrings.append(substring)
    
    return substrings

input_sec = input("pon la secuencia: ")
input_n = int(input("pon el valor de n: "))

substrings_u = o_substrings_u(input_sec, input_n)

if len(substrings_u) == 0:
    print("ninguna")
else:
    for substring in substrings_u:
        print(substring)