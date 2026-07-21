def greet(name):
    print("hello " + name)

    print("1.value of name in greet is:" + name)
    name = "fab"
    print("2.value of name in greet is:" + name)

def main():
    name = "barawa"
    print("1.value of name in main is:" + name)
    greet(name)
    print("2.value of name in main is:" + name)

main()
