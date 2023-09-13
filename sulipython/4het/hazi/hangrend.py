mely, magas, vegyes, semmilyen = range(4)


def main():

    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]

    mely0 = 'a'
    mely1 = 'á'
    mely2 = 'o'
    mely3 = 'ó'
    mely4 = 'u'
    mely5 = 'ú'

    magas ='eéiíöőüű'

    for i in words:
        if mely0 in i or mely1 in i or mely2 in i or mely3 in i or mely4 in i or mely5 in i:
            print(i + " mély")


if __name__ == '__main__':
    main()