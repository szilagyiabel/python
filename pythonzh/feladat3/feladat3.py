def main():

    dict = {}
    f = open("hibas_bevasarlo_lista.txt","r")
    lines = [line.rstrip("\n") for line in f.readlines()]

    for line in lines:
        line = line.rstrip("\n")

        if line.split(" - ")[0] not in dict:
            dict[line.split(" - ")[0]] = int(line.split(" - ")[1])
        else:
            dict[line.split(" - ")[0]] += 1

    r = open("bevasarlo_lista.txt","w")

    for i in dict.items():
        r.write(str(i[0]) + '-' + str(i[1]) + "\n")

    f.close()
    r.close()


if __name__ == '__main__':
    main()