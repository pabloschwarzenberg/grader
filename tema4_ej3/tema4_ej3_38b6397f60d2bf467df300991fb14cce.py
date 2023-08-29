def jerigonzo(string):
    que="aeoiuAEOIU"
    let=""
    for x in range(len(string)):
        if string[x] in que:
            let+=string[x]+"p"+string[x]
        else:
            let+=string[x]
    return let

    

      