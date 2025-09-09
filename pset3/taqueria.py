menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_order(items):
    check_item = input("Item: ")

    if check_item in menu:
        print(check_item)



def main():
    total_cost = get_order()
    print("Total:", total_cost)

if __name__ == "__main__":
    main()
