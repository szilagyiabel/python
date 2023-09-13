def main():

    f = open("random2.txt", "r")
    f0 = open("tippek2.txt", "r")
    i = 0
    eltalalt = 0
    nemjo = 0

    for line in f:
        line = line.rstrip("\n")
        if int(line) > 50:
            nemjo += 1
            pass
        for line0 in f0:
            line0 = line0.rstrip("\n")
            if line[i] == line0[i]:
                eltalalt += 1
            
            
        print(line0)
        #print(line)
        i += 1

    print('Eltalált számok:', eltalalt, 'az összes', i - nemjo, 'helyesen generalt szamokból.')
    print(nemjo)
    f.close()
    f0.close()

if __name__ == '__main__':
    main()