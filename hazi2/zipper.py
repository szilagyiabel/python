def main():

    chars = "abcdefghijklmnopqrstuvwxyz"
    codes = list(range(ord('a'), ord('{')))
    
    i = 0

    for t in codes:
        print('('+ "'" + chars[i] + "'" + ',' , t, ')')
        i += 1

if __name__ == "__main__":
    main()