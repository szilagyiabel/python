def main():

    szamok = 73167176531330624919225119674426574742355349194934
    
    index = 0
    n = 0

    for i in range(szamok):
        
        n = i[index] * i[index + 1] * i[index + 2] * i[index + 3] * i[index + 4]
        index += 1
        
        print(n)
        

if __name__ == '__main__':
    main()