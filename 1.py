def concat(kakulka, *popa, reversed: bool = False):
    if reversed==False:
        kakushka = ''
        for a in popa:
            kakulka += a
        kakushka = kakulka
    else:
        kakushka = ''                                                                                                                                                                                                                                                                               #1000-7=?
        for a in range(len(popa)-1,-1,-1):
            kakushka += popa[a]
        kakushka += kakulka
    print(kakushka)

concat('300', ' ', 'bucks',  reversed=True)