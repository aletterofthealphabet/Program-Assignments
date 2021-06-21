## This program is to practice using python dictionaries

# Initalize a menu with name of item and prices
#     Key      : value
# Name of item : price
menu = {"Chicken" : 1.59, 
        "Beef" : 1.99, 
        "Cheese" : 1.00,
        "Milk" : 2.50}

# Initalize a menu with name of item and prices
#        Key        : value
# Name of character : TV Show
tv_characters = {"Tulip Olsen" : "Infinity Train",
                 "Marcy Wu" : "Amphibia",
                 "Luz Noceda": "The Owl House",
                 "Wirt" : "Over the Garden Wall"}

# Get the prices from the menu
chicken_price = menu["Chicken"]
beef_price = menu["Beef"]
cheese_price = menu["Cheese"]
milk_price = menu["Milk"]

# Print out all the menu values
print("\n")                                                  # Convension Preference, Used to seperate different topics
print("The chicken price is $" + str(chicken_price) + ".")   # Typecasting to avoid an error
print("The beef price is $" + str(beef_price) + ".")
print("The cheese price is $" + str(cheese_price) + ".")
print("The milk price is $" + str(milk_price) + ".")

# Get the TV shows from tv_characters
tulip_olsens_show = tv_characters["Tulip Olsen"]
marcy_wus_show = tv_characters["Marcy Wu"]
luz_nocedas_show = tv_characters["Luz Noceda"]
wirts_show = tv_characters["Wirt"]

# Print our all the tv character's shows
print("\n")                                                 # Convension Preference, Used to seperate different topics
print("Tulip Olsen is from " + tulip_olsens_show + ".")
print("Marcy Wu is from " + marcy_wus_show + ".")
print("Luz Noceda is from " + luz_nocedas_show + ".")
print("Wirt is from " + wirts_show + ".")

# Initalize a variable with shoes names and their inventory
#      Key     :      value
# Name of Shoe : Number of item
shoes_and_inventory = {"Jordan 13" : 1,
                       "Yeezy" : 8,
                       "Foamposite" : 10,
                       "Air Max": 5,
                       "SB Dunk": 20}

# Update the value of the inventory

# Costumer has purchased 2 pairs of Yeezys
shoes_and_inventory["Yeezy"] -= 2

# Costumer returned a pair of Yeezys
shoes_and_inventory["Yeezy"] += 1

# Store receieves new shipment +7 to all
shoes_and_inventory["Jordan 13"] += 7
shoes_and_inventory["Yeezy"] += 7
shoes_and_inventory["Foamposite"] += 7
shoes_and_inventory["Air Max"] += 7
shoes_and_inventory["SB Dunk"] += 7

# Special Sale, all stocks decrease by 3
shoes_and_inventory["Jordan 13"] -= 3
shoes_and_inventory["Yeezy"] -= 3
shoes_and_inventory["Foamposite"] -= 3
shoes_and_inventory["Air Max"] -= 3
shoes_and_inventory["SB Dunk"] -= 3

# Add 2 items to every dictionary: menus, tv_characters and shoes_and_inventory
# Menu
menu["Egg"] = 1.05
menu["Cream"] = 2.69

# Tv_characters
tv_characters["Anne Boonchuy"] = "Amphibia"
tv_characters["Lake"] = "Infinity Train"

# shoes_and_inventory
shoes_and_inventory["Converse"] = 4
shoes_and_inventory["Jordan 1"] = 5

# Delete 2 items from every dictionary: menus, tv_characters and shoes_and_inventory
del menu["Egg"] 
del menu["Cream"] 
del tv_characters["Anne Boonchuy"]
del tv_characters["Lake"]
del shoes_and_inventory["Converse"]
del shoes_and_inventory["Jordan 1"]

# Lab 4
# Create a function that adds 2 menu prices from menu
def total_price(*foodItems):

        """Returns the total price of a given food"""
        foodItems = list(foodItems)

        for item in foodItems:                          # Check if items are on the menu
                if item not in menu:
                        return "Error: One or more of the foods is not on the menu"

        # Calculate the total
        total = 0
        for item in foodItems:
                total = menu[item]
        
        # Return the price of the items combined based on the menu
        to_be_returned = "The total price of "

        for item in foodItems:
                to_be_returned += item
                if(item != foodItems[-1]):
                        to_be_returned += " and "
        
        to_be_returned += " "
        to_be_returned += str(total)
        to_be_returned += "."

        return to_be_returned    

def price_difference(foodItem1 = "NA", foodItem2 = "NA"):
        
        """Returns the price difference between 2 foods"""

        if(foodItem1 == "NA" or foodItem1 == "NA"):
                return "Error: One or more food items not listed"
        elif ((foodItem1 not in menu) or (foodItem2 not in menu)):
                return "Error: One or more food items is not in menu"
        
        difference = menu[foodItem1] - menu[foodItem2]

        return abs(difference)

def restock(shoe_name, multiplier):
        newInv = shoes_and_inventory[shoe_name] * multiplier
        shoes_and_inventory[shoe_name] = newInv
        return shoes_and_inventory

def clearance(shoe_name, discount):
        salePrice = shoes_and_inventory[shoe_name] / discount
        shoes_and_inventory[show_name] = salePrice
        return shoes_and_inventory