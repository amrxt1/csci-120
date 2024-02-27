#815257

inventory = {}

def get_item(prompt):
    while True:
        item = input(prompt)
        if item and item != "":
            return item
        print("Item name is invalid, try again")

def get_value(prompt):
    while True:
        val = input(prompt)
        try:
            return int(val)
        except ValueError:
            print("Please enter a numeric value.")
            continue

def add_item():
    item = get_item("Please enter the item: ")
    value = get_value("Please enter the value: ")
    inventory[item] = int(value)
    display_inventory()

def remove_item():
    #Avoid using loop to prevent a stuck-in-loop condition in case item not in list
    item = get_item("Please enter the item to delete: ")
    if item in inventory.keys():
        del inventory[item]
    else:
        print("Item not in inventory")
    display_inventory()
    

def display_inventory():
    print("\nCurrent Inventory:")
    
    for key in inventory:
        print(str(key) +": "+str(inventory[key]))
    print("")

def ask_question():
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display current inventory")
    print("4. Exit")
    return input("\n> ")

def main():
    print("\nWelcome to the inventory management system!\n")
    while True:
        answer = ask_question().strip()
        if answer == '1':
            add_item()
        elif answer == '2':
            remove_item()
        elif answer == '3':
            display_inventory()
        elif answer == '4':
            return
        else:
            print("Invalid choice, try again\n")
            continue

main()