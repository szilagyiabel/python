import prim

def main():
    
    for i in range(100):
        if prim.is_prime(i):
            pass
    
    szamok = {i for i in range(100) if prim.is_prime(i)}
    print(szamok)

if __name__ == '__main__':
    main()