
def main():
    jegyek = {'otos': 0, 'negyes': 0, 'harmas': 0, 'kettes' : 0, 'egyes' : 0}
    f = open("jegyek.txt", "r")

    ct = 0
    sum = 0        

    for line in f:
        line = line.rstrip("\n")
        pont = float(line.split()[3])

        if line.endswith("4.0"):
            jegyek['otos'] += 1
        elif line.endswith("3.5"):
            jegyek['otos'] += 1
        elif line.endswith("3.0"):
            jegyek['negyes'] += 1
        elif line.endswith("2.5"):
            jegyek['harmas'] += 1
        elif line.endswith("2.0"):
            jegyek['kettes'] += 1
        else:
            jegyek['egyes'] += 1
        ct += 1
    sum += 5*jegyek['otos'] + 4*jegyek['negyes'] + 3*jegyek['harmas'] + 2*jegyek['kettes']+jegyek['egyes']

    
    print('Egyes - ', jegyek['egyes'])
    print('Kettes - ', jegyek['kettes'])
    print('Hármas - ', jegyek['harmas'])
    print('Négyes - ', jegyek['negyes'])
    print('Ötös - ', jegyek['otos'])
    print('gecis átlag - ', sum/ct)

    f.close()

if __name__ == '__main__':
    main()