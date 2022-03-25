def concat(a, *args, reversed: bool = False):
    if reversed==False:
        b = ''
        for i in args:
            a += a
        b = a
    else:
        b = ''                                                                                                                                                                                                                                                                               #1000-7=?
        for a in range(len(args)-1,-1,-1):
            b += args[i]
        b += a
    print(b)

concat('Hello', ' ', 'World',  reversed=True)
