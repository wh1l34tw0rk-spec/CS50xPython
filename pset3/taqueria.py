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


def get_order(item):
       while True:
        try:
            item_ordered = item.title()
            if item_ordered in menu:
                price = float(menu[item_ordered])
                total = price
                print(total)
        except EOFError:
            return item



def main():
    total = get_order(input("Item: "))
    print(total)
# need to figure out prompt and how to repeat asking + update price



if __name__ == "__main__":
    main()
