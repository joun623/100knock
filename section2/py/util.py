def open_hightemp():
    with open ("hightemp.txt") as fin:
        hightemp = fin.read()

    return hightemp


