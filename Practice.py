with open ("text.txt", 'r') as fi:
    while 1:
        line = fi.readline()
        if line == "":
            break
        print(line)