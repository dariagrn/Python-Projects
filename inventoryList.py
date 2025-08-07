#Programmer: Daria Green
#Email: Daria.green20@gmail.com
#Purpose: Market Items Inventory List

#Items I offer
itemName =[
    'Mystery Pouch',
    'Bead KeyChain',
    'Book Sleeve',
    'Bandana',
    'Amigurumi Sticks',
    'Opctopus Plushy',
    'Mushroom Fidget Toy',
    'Rosette Purse (Small)',
    'Rosette Purse (Large)',
    'Granny Square XL Purse',
    'Peach Granny Square Purse',
    'Sparkle Blue Totebag',
    'Bow Clip',
    'Spa Set',
    'Pumpkin Plushy',
    'Flower Coaster Set',
    'Pencil Pouch',
    'Mushroom Pillow',
    'Granny Square Runner',
    'Crochet Blanket'
]

inventoryAmount =[
    '30',
    '12',
    '10',
    '10',
    '15',
    '7',
    '15',
    '5',
    '5',
    '1',
    '1',
    '1',
    '15',
    '10',
    '10',
    '5',
    '5',
    '5',
    '2',
    '2'
]

price =[
    '10',
    '12',
    '20',
    '10',
    '15',
    '10',
    '10',
    '45',
    '55',
    '90',
    '40',
    '55',
    '10',
    '35',
    '25',
    '25',
    '12',
    '70',
    '100',
    '300'
]

print("\nWelcome to Daria's Market Inventory List")
print("Here are the items I have available for sale:")

#item listing printed. with the statement below
for i in range(len(itemName)):
    print(f"\n{itemName[i]}")

#ask user to select an item to display details
print("\nPlease enter the name of the item you would like to purchase:")
item = input().strip()

#if/else statement to display the item details the user chose or presented with Item not found
if item in itemName:
    index = itemName.index(item)
    print(f"\nYou have selected {item}.")
    print(f"\nPrice: ${price[index]}")
    print(f"\nAvailable Inventory: {inventoryAmount[index]}")
else:
    print("\nItem not found.")

print("\nWould you like to order this item? (yes/no)")
order = input().strip().lower()
if order == "yes":
    print(f"\nThank you for your order of {item}.")
else:
    print("\nOrder canceled.")