#to do
def show_menu():
    select=("display database", "add item", "delete item", "change item", "quit program")
    for i in range(0, len(select)):
        print(str(i + 1) + ": " + select[i])


def display_database(database):
    for i in range(0, len(database)):
        print(str(i + 1) + ": " + database[i])

def add_item(database):
    item=input("Enter the item to add: ")
    database.append(item)

def delete_item(database):
    deleted=input("Enter the number of item to be deleted: ")
    database.pop(int(deleted))
    

def change_item(database):
    changed=input("Enter the number of item to be changed: ")
    new_item=input("Enter the new item: ")
    database[int(changed)]=new_item



def main():
    database=["ugali", "sukuma", "nyama", "chapati"]

    do_loop=True
    while do_loop:
        show_menu()
        

        option=input("Enter your option: ")
        if option=="1":
            display_database(database)
        elif option=="2":
            add_item(database)
        elif option=="3":
            delete_item(database)
        elif option=="4":
            change_item(database)
        elif option=="5":
            do_loop=False
        else:
            print("Invalid option. Please try again.")
        print()

main()
