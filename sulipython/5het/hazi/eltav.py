def main():

    a = """
        A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

        A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

        A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre
    """

    print(a.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ü', 'u').replace('ö', 'o').replace('ó', 'o').replace('ű', 'u').replace('ő','o').replace('ú', 'u'))


if __name__ == '__main__':
    main()