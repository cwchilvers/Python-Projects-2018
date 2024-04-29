import csv



def double_line():
    print("==========================================================================")

def single_line():
    print("--------------------------------------------------------------------------")

def new_screen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")



def display_inventory():
    file = open("inventory.csv", "r")
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " | ", "Total:", row[1], " | ", "Available:", row[2], " | ", "In Use:", row[3])
    file.close


room = "Main Menu"





while True:
    
    while room == "Main Menu":
        new_screen()
        double_line()
        print(" M A I N   M E N U")
        single_line()
        print(" - Press \"I\" to display inventory")
        user_selection = input("")

        if user_selection.lower() == "i":
            room == "Inventory"
            break
        
    while room == "Inventory":
        new_screen()
        double_line()
        print(" I N V E N T O R Y")
        single_line()
        display_inventory()
        input("")
