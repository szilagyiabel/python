def main():

    a = list(str(pow(2,1000)))
    
    osszeg = 0

    for i in range(len(a)):    
        osszeg += int(a[i])

    print(osszeg)

if __name__ == '__main__':
    main()