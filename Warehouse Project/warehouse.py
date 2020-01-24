from menu import print_menu
from item import Item
import datetime
import pickle
import os

logs = []
items = []
id_count = 1
items_file = "item.data"
logs_file = "logs.data"

# def clear():
    # return os.system("cls")

def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%X")
    return time

def save_items():
    writer = open(items_file, "wb")
    pickle.dump(items, writer)
    writer.close()
    print("Congrats, Your Data Has Been Saved!")

def save_log():
    writer = open(logs_file, "wb")
    pickle.dump(logs, writer)
    writer.close()
    print("Oh, Hey, Look, You Saved The Log! *High five*")

def read_items():
    global id_count

    try:
        reader = open (items_file, "rb")
        temp_list = pickle.load(reader)

        for item in temp_list:
            items.append(item)

        last = items[-1]
        id_count = last.id + 1
        print(" Loaded: " + str(len(temp_list)) + " items")
    except:
        print("*Oooops: The data count not be loaded :( You should probably fix that")

def read_log():
    try:
        reader = open(logs_file, "rb")
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)

        print(" Loaded: " + str(len(temp_list)) + " log events")

    except:
        print("*Oooops: The data count not be loaded :( You should probably fix that")

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):
    print_header(header_text)
    print("-" * 70)
    print("ID  | Core Material             | House           | Price     | Stock")
    print("-" * 70)

    for item in items:
        print(str(item.id).ljust(3) + " | " + item.title.ljust(25) + " | " + item.category.ljust(15)+ " | " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))

def register_item():
    global id_count

    print_header("Register New Items")
    title = input ("Core Material?")
    category = input ("To which Hogwarts house does the wand Owner belong?: ")
    price = float(input("Price in Galleons: "))
    stock = int(input("How many wands are currently in stock? "))

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    
    id_count += 1
    items.append(new_item)
    print(" Item Created!!")



def update_stock():
    print_all("Choose an Item from the list")
    id = input("\nSelect an ID to update stock: ")
    found = False 
    for item in items:
        if(str(item.id) == id):
            stock = input("Please input new stock value: ")
            item.stock = int(stock)
            found = True

            log_line = get_time() + " | Update | " + id
            logs.append(log_line)
            save_log()

    if(not found):
        print("**Error: ID doesn't exist. Try Again!")

def remove_item():
    print_all("Choose an Item to Remove")
    id = input("\nSelect an ID to remove: ")

    for item in items:
        if(str(item.id) == id):
            items.remove(item)
            print("Item has been removed!")

def list_no_stock():
    print_header("Items with no stock")
    for item in items:
        if(item.stock == 0):
            print(item.title)

def print_categories():
    temp_list = []

    for item in items:
        if(item.category not in temp_list):
            temp_list.append(item.category)

    print(temp_list)

def register_purchase():
    print_all("Time to Restock. What did we get more of?")
    id = input("\nSelect an Item to update stock numbers: ")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many wands did we buy this time?: ")
            item.stock +=int(stock)
            found = True

        if(not found):
            print("**Error: ID doesn't exist. Try Again!")

def register_sell():
    print_all("Oh, hey, look who made a sale. *high five*")
    id = input("\nSelect an Item and watch that stock number go down: ")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many did we sell?: ")
            item.stock -=int(stock)
            found = True

        if(not found):
            print("**Error: ID doesn't exist. Try Again!")

def print_stock_value():
    total = 0.0
    for item in items:
        total += (item.price * float(item.stock))

        print("Stock value: " + str(total))

def print_log():
    read_log()
    for log in logs:
        print(log)
        



read_items()
read_log()

opc = ''
while(opc != 'x'):
    # clear()
    print_menu()

    opc = input("Please select an item: ")

    if(opc == "1"):
        register_item()
        save_items()
    elif(opc == "2"):
        print_all("List of all items")
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        list_no_stock()
    elif(opc == "5"):
        remove_item()
        save_items()
    elif(opc == "6"):
        print_categories()
    elif(opc == "7"):
        print_stock_value()
    elif(opc == "8"):
        register_purchase()
    elif(opc == "9"):
        register_sell()
    elif(opc == "10"):
        print_log()
    if(opc != 'x'):
        input("\n\nSwish and Flick to continue")
