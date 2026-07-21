def factorial(value):

    result = 1

    for i in range(2, value + 1):
        result = result * i

    return result

def main():
    result=factorial(5)

    print("result:", result)

main()
