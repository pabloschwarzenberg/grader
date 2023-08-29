def comp_adn(adn1, adn2):

    adn3 = '' # ___TG_______A__C_G__TT_C_AGTAGTCGATT

    j = 0

    for n, i in enumerate(adn2):
        if j < len(adn1):
            for m, k in enumerate(adn1[j:]):
                j += 1
                if k == i:
                    adn3 += i
                    break
                else:
                    adn3 += '_'
        else:
            adn3 += adn2[n:]
            break

    return adn3


adn3 = comp_adn(input(), input())

print(adn3)
    #print(adn3 == '___TG_______A__C_G__TT_C_AGTAGTCGATT')



