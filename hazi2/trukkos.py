
def main():
    tmp=[]
    with open("b.txt", "r") as f:
        lines = [ line.strip() for line in f.readlines()]
    for line in lines:
        print("".join([chr(int(x, 2)) for x in line.split(" ")]))
        tmp.append("".join([chr(int(x, 2)) for x in line.split(" ")]))
        
if __name__ == '__main__':
    main()