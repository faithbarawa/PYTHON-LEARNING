PASSWORD="fab"

def check_user_password():
    password=input("Enter your password: ")
    if password==PASSWORD:
        print("Access granted")
    else:
        print("Access denied")


def main():
    check_user_password()   
main()