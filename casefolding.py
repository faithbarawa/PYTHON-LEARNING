#to do:apply casefolding
def user_loop(people):
    people_cf={name.casefold(): age for name, age in people.items()}
    while True:
        name=input("Enter your name: ")
        if name.casefold() not in people_cf:
            print("Name not found in the database.")
        if name.casefold() in people_cf:
            print("Your age is: " + str(people_cf[name.casefold()]))

        if name=="quit":
            break

def main():
    people={
        "Amelia":20,
        "Arthur":30,
        "Isla":25,
        "Noah":65,
        "Ava":21,
        "Leo":70,
        "Mia":32,
        "Oscar":45,
    }
    user_loop(people)
main()
