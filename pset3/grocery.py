def add_item(list):
    # Take in user input until opted out
    # Append input to a list
    # Iterate through list to find number of times item was inputted
    # Return list in alphabetical order
    return list.upper()


def main():
    print("Organize your grocery list once and for all!")
    start_list = input("Enter Item: ")
    grocery_list = add_item(start_list)
    print(grocery_list)

if __name__ == "__main__":
    main()
