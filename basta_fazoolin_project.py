# Create a Menu class
class Menu:
  # Give Menu a constructor with five parameters self, name, items, start_time and end_time
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  # Give the Menu class a string representation method that will tell you the name of the menu and when the menu is available
  def __repr__(self):
    return ('{} menu available from {} to {}').format(self.name, self.start_time, self.end_time)
  
  # Give Menu a method .calculate_bill() that has two parameters: self, and purchased_items, a list of the names of purchased items
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
  # Have calculate_bill return the total price of a purchase consisting of all the items in purchased_items
    return total

 # Create the first menu: brunch   
brunch = Menu('brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

# Create a second menu item: early_bird
early_bird = Menu('early-bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)
# Create a third menu item: dinner
dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

# Create the penultimate menu item: kids
kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

# Create the last menu item: arepas_menu
arepas_menu = ('arepas menu', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)

# Print out the string representation
print(brunch)

# Test out Menu.calculate_bill() by passing in one order of pancakes, one order of home fries and one coffee
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))# Prints 13.5

# Test out the function with an early-bird purchase
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])) # Prints 21.5

# Create a Franchise class
class Franchise:
  # Give the Franchise class a constructor which takes in an address, and a list of menus
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  # Give the Franchise class a string representation so that we can tell the different restaurant addresses apart
  def __repr__(self):
    return 'The address of the franchise is {}'.format(self.address)
  
  # Give Franchise an .available_menus() method that takes in a time parameter and returns a list of the Menu objects that are available at that time
  def available_menus(self, time):
    available_menu_names = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu_names.append(menu.name)
    return available_menu_names
# Define a Business class
class Business:
  # Give Business a constructor with name name and a list of franchises
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
# Create your first two franchises: the flagship store is located at '1232 West End Road' and the new installment is located at '12 East Mulberry Street'
# Pass in all four menus into each establishment
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 Mulberry Street', [brunch, early_bird, dinner, kids])

# Create the Take a' Arepa franchise located at '189 Fitzgerald Avenue'
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

# Test that the string representation method works
print(flagship_store)
print(new_installment)
print(arepas_place)

# Test that the .available_menus() method works
print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))

# Create a Business instance - name: 'Basta Fazoolin' with my Heart', franchises: flagship_store and new_installment
new_basta_fazoolin_business = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

# Create a new Business - 'Take a' Arepa'
new_take_a_arepa_business = Business('Take a\' Arepa', [flagship_store, new_installment])
