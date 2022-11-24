# preparar una taza de cafe
# inicia en taza, cafe y agua caliente para usar = true
# inputs opcionales: milk, cream y sugar
#

# ingredientes_fundamentales = {

# }
menu = {
    1: {"name": 'cup',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'hot water', 
        "price": 2.79},
    # 4: {"name": 'soup', 
    #     "price": 4.50},
    # 5: {"name": 'sandwich',
    #     "price": 4.99}
}


def calculate_subtotal(order):


    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = 0
    for itemMenu in order:
        subtotal += itemMenu['price']
    return round(subtotal, 2)

    raise NotImplementedError()

def calculate_tax(subtotal):

    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tasa = 15
    return round((subtotal * tasa) / 100, 2)
    raise NotImplementedError()

def summarize_order(order):

    print_order(order)
    ### WRITE SOLUTION HERE
    listName = []
    for item in order:
         listName.append(item['name'])
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(calculate_subtotal(order))
    total = round(subtotal + tax, 2)
    return listName, total
    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)
    print("Pedido", items)
    print("Total", subtotal)

if __name__ == "__main__":
    main()
