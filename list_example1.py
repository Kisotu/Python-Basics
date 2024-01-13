inventory = ['apples', 'bananas', 'oranges', 'pawpaws', 'carrots', 'dates', 'pineapples']


# func to display list
def show_inventory():
    print("Current Inventory:")
    for item in inventory:
        print(f"- {item}")


def add_item(item):
    inventory.append(item)
    print(f"'{item}' has been added to the inventory.")


def remove_item(item):
    if item in inventory:
        inventory.remove(item)
        print(f"'{item}' has been removed from the inventory")
    else:
        print(f"'{item}' is not in the inventory")


show_inventory()
add_item('eggplant')
remove_item("dates")
show_inventory()
