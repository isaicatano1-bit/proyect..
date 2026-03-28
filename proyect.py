
import csv

its_ok = True
products = []
inventory =[]



def add_product():
    ok = True
    name = input("enter name of product: ").lower()
    while ok:
        try:
            quantity = int(input("enter the quantity of product : "))
            if quantity <=0:
                print("ERROR. enter a valid number")
            else:
                break
        except ValueError:
            print("not enter a character")
    while ok:
        try:
            price = float(input("enter the price of product: "))
            if price <=0:
                print("ERROR. enter a valid number")
            else:
                 break
        except ValueError:
            print("not enter a character")
    
    product ={
        "name" : name,
        "quantity" : quantity,
        "price" : price
    }
    inventory.append(product)
    return



#explain sells

def show_inventory():
    if len(inventory) == 0:
        print("inventory empty")
        return

    for product in inventory:
        print("Name:", product["name"])
        print("Price:", product["price"])
        print("Quantity:", product["quantity"])
        print("----------------")



def load_csv():
    try:
        with open("inventory.csv", mode="r", newline="") as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                inventory.append({
                    "name": fila["name"],
                    "price": float(fila["price"]),
                    "quantity": int(fila["quantity"])
                })
    except FileNotFoundError:
        print("archive no found, creating a new archive.")

def save_csv():
    with open("inventory.csv", mode="w", newline="") as archivo:
        campos = ["name", " ","price"," " ,"quantity"]
        writer = csv.DictWriter(archivo, fieldnames=campos)

        writer.writeheader()
        for product in inventory:
            writer.writerow(product)





def update_product():
    name = input("enter product name to update: ").lower()

    for product in inventory:
        if product["name"] == name:

            while its_ok:
                try:
                    new_quantity = int(input("enter new quantity: "))
                    if new_quantity < 0:
                        print("ERROR. invalid number")
                    else:
                        product["quantity"] += new_quantity
                        print("product updated")
                        return
                except ValueError:
                    print("not a number")

    print("product not found")

def serch_product():
    name = input("Enter product name: ").lower()

    for product in inventory:
        if product["name"] == name:
            print("Product found:")
            print("Name:", product["name"])
            print("Quantity:", product["quantity"])
            return

    print("Product not found")

def calculate_stats():
    if len(inventory) ==0:
        print("inventory empty")
        return
    total_quantity = 0
    total_price = 0
    for product in inventory:
        total_quantity += int(product["quantity"])
        total_price += float(product["price"])
        total_of_products = total_price * total_quantity

    print("total products: ",len(inventory))
    print("total quantity: ", total_quantity)
    print("total price: ",total_price)
    print("total: ", total_of_products)

    most_expensive = inventory[0]

    for product in inventory:
        if product["price"] > most_expensive["price"]:
            most_expensive = product

    print("most expensive product:", most_expensive["name"])
    print("price:", most_expensive["price"])

    most_quantity = inventory[0]

    for product in inventory:
      if product["quantity"] > most_quantity["quantity"]:
        most_quantity = product

    print("product with most quantity:", most_quantity["name"])
    print("quantity:", most_quantity["quantity"]) 



    

#menu
while its_ok:
    print("-----------------------------------------")
    print("WELCOME TO THE MENU")
    print("")
    print("-----------------------------------------")
    print("1. add product")
    print("2. stats")
    print("3. update product")
    print("4. search product")
    print("5. show inventory")
    print("6. save csv")
    print("7. load csv")
    print("8. exit")
    option = input("enter a option: ")
    print("")


    if option == "1":
        add_product()
    elif option == "2":
        calculate_stats()
    elif option == "3":
        update_product()
    elif option == "4":
        serch_product()
    elif option =="5":
        show_inventory()
    elif option == "6":
        save_csv()
    elif option == "7":
        load_csv()
    elif option == "8":
        print("welcome soon")
        break
    else:
        print("ERROR. enter a valid option")
