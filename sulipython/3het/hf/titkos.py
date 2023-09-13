def main():

    a = """
    Cbcq Dgyk!

    Dmeybh kce cew yrwyg hmrylyaqmr:
    rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

    Aqmimjjyi:

    Ynyb"""

    b = []
        
    for i in range(len(a)):
        if a[i] in ('\n', '!', ' ', ':'):
            b.append(a[i])
            continue
        elif a[i] in ('z', 'y','Y','Z'):
            b.append(chr(ord(a[i]) - 24))
            continue
        b.append(chr(ord(a[i]) + 2))

    print(''.join(b))

if __name__ == '__main__':
    main()