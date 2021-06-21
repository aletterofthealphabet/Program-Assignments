# Initalize list of city names
city_names = ["Oakland", "Atlanta", "New York City",        # For convention
              "Seattle", "Memphis", "Miami", 
              "Boston", "Los Angeles", "New Orleans"]

# Initalize list of musical names
musicals = ["In the Heights", "Aladdin", "Mean Girls",      # For convention
            "Dear Evan Hansen", "Be More Chill", "Matilda",
            "Hadestown", "Hairspray", "Legally Blonde",
            "West Side Story"]

# Print out names of favorite musicals x 3
print(musicals[3])
print(musicals[4])
print(musicals[-5])

# Use list splicing to get the favorite musicals listName[inclusive:exclusive]
favorite_musicals = musicals[3:6]

# Print out your favorite musicals
print("\n")                                                  # For convention
for musical in favorite_musicals:
    print (musical)

# Edit city names
city_names[0] = "San Francisco"     # Oakland --> San Francisco
city_names[2] = "Brooklyn"          # New York City --> Brooklyn
city_names[7] = "Hollywood"         # Los Angeles --> Hollywood
city_names[5] = "Tampa"             # Miami --> Tampa

# Add to city names
city_names.append("Houston")
city_names.extend(["New Jersey", "Chicago"])    # Extend addes two list together
city_names.insert(7, "D.C.")

# Delete some city names
city_names.pop(0)                   # Removes San Francisco
del city_names[7]                   # Removes D.C
city_names.remove("Tampa")

# Loop Practice
# Using a function
# Print out all the values in city_names
# Using a while loop to update index
# Make sure that index is less than list length

def printList(name_of_list):
    """Prints all the values in a selected list"""

    temp_counter = 0
    while (temp_counter < len(name_of_list)):
        print(str(temp_counter) + ": " + str(name_of_list[temp_counter]))   # Results in index : value
        temp_counter += 1

    return "Program successfully executed"

printList(city_names)