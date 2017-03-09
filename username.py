# username.py
def main():
    # Get user’s first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # concatenate first initial with
    # 7 chars of last name
    uname = first[0] + last[:7]
    print("Your username is:",uname)

main()
