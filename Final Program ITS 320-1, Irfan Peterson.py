#------------------------------------------------------------------------
# Program Name: Week 2 Assignment, ITS320_CTA2_Option2
# Author: Irfan Peterson
# Date:12/22/2019
#------------------------------------------------------------------------
# Pseudocode: 1)Inputs entered by end user.
#             2)How the data is stored.
#             3)Which the data is printed on the screen.                      
#------------------------------------------------------------------------
# Program Inputs: Tesla, Model 3, 2018, 56, 16000, 100
# Program Outputs:{'car': 'Tesla', 'car model': 'Model 3', 'year': 2018, 'starting odometer': 56.0, 'ending odomoter': 16000.0, 'miles per gallon': 100.0}
#------------------------------------------------------------------------

class Vehicle:
    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def __str__(self):
        print('-----------------------------------')
        return('Make: %s \nModel: %s \nColor: %s Year: %d \nMileage: %d' % (self.make, self.model, self.color, self.year, self.mileage))
            
    def edit_vehicle(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

def add_vehicle(v_inventory):
    make = input('Enter Make: ')
    model = input('Enter Model: ')
    color = input('Enter Color: ')
    year = int(input('Enter Year: '))
    mileage = int(input('Enter Mileage: '))
    auto = Vehicle(make, model, color, year, mileage)
    v_inventory.append(auto)

def remove_vehicle(v_inventory):
    position = int(input('Enter Vehicle Position To Be Removed: '))
    v_inventory.pop(position)

def update_vehicle(v_inventory):
    position = int(input('Enter Vehicle Position To Be Updated: '))
    print('Enter New Details of the Vehicle')
    make = input('Enter Updated Make: ')
    model = input('Enter Updated Model: ')
    color = input('Enter Updated Color: ')
    year = int(input('Enter Updated Year: '))
    mileage = int(input('Enter Updated Mileage: '))
    v_inventory[position-1].edit_vehicle(make, model, color, year, mileage)

def print_vehicle(v_inventory):
    for i in v_inventory:
        print(i)
        print('-----------------------------------')

def write_to_text(v_inventory):
    my_file = open('vehicle_inventory.txt', 'w')
    for i in v_inventory:
        my_file.write(str(i))
    my_file.close()

v_inventory = []

user = True
while user:
    print("""
Vehicle Inventory Options
-------------------------
1.) Add New Vehicle
2.) Remove Existing Vehicle
3.) View Current Inventory
4.) Update Vehicle Inventory
5.) Export Current Inventory List
6.) Exit, Thank you!  
    """)

    inventory_option = int(input('Please Enter Inventory Option: '))

    if inventory_option == 1:
        add_vehicle(v_inventory)

    elif inventory_option == 2:
        remove_vehicle(v_inventory)

    elif inventory_option == 3:
        print_vehicle(v_inventory)

    elif inventory_option == 4:
        update_vehicle(v_inventory)

    elif inventory_option == 5:
        write_to_text(v_inventory)

    elif inventory_option == 6:
        user = False

    else:
        print('Invalid Option, Please Enter Option 1-5, Thank you')

