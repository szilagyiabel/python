class EmptyClass:
    pass

class MyClass:
    def hello(self):
        return "Hello"

def main():
    obj = MyClass()
    print(obj.hello())

if __name__ == '__main__':
    main()