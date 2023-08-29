largo = int(input())

def bins(string, largo):
    if len(string) == largo:
        print(string)
        return
    bins(string + "0", largo)
    bins(string + "1", largo)
    return
bins("", largo)
           