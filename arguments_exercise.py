def test(name, *args, **kwargs):
    print(name)
    print()

    for arg in args:
        print(arg)

    print()

    for key in kwargs:
        print(key, "=", kwargs[key])

        





def main():
    test("barawa", "fab", "bar", "foo", complexion="fair", height="6feet", weight="70kg")

main()