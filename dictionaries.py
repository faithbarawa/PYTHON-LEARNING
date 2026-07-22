#keys can have values......when paired its an item or entry
#keys are unique
#to add values ,months["January"]="Jan" or months.update({"January":"Jan"})
#to delete items,del months["January"] or months.pop("January")
#gett function used to retrieve values....color=(fruits.get("item in your dictionary")) if there is no item, you pass a value to it
#you can import a default dict so that you dont get an error when
#do it by from collections import defaultdict
#to copy in dictionaries, fruits2={key:value for(key, value)in fruits,items()} ()

def user_loop(people):
    while True:
        name=input("Enter your name: ")
        if name not in people:
            print("Name not found in the database.")
        if name in people:
            print("Your age is: " + str(people[name]))

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
