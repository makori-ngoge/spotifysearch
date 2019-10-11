def commafy(num):
    num = str(num)
    split = []
    final = ""
    index = len(num) % 3

    if len(num) > 3:
        if index == 0:
            index += 3
        for x in num:
            split.append(x)
        while index < len(split):
            split.insert(index, ",")
            index += 4
        for x in split:
            final += x
        print(final)
    else:
        print(num)
    

commafy(7000)
commafy(80000)
commafy(35000000)