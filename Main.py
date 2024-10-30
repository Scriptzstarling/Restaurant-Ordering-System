# Main.py

from Menu_data import menu  

# Display greeting and the menu.
print("Welcome to our restaurant! Here is our menu:\n")

print("Appetizers:")
print("Garlic Bread: Rs30\nFrench Fries: Rs35\nOnion Rings: Rs40\nMozzarella Sticks: Rs50\n")

print("Main Courses:")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs80\nGrilled Sandwich: Rs45\nVeggie Wrap: Rs55\nChicken Wings: Rs70\n")

print("Beverages:")
print("Coffee: Rs100\nTea: Rs80\nIced Lemonade: Rs90\nMango Smoothie: Rs120\nCoke: Rs60\nOrange Juice: Rs70\n")

print("Desserts:")
print("Chocolate Cake: Rs150\nIce Cream Sundae: Rs130\nCheesecake: Rs140\nBrownie: Rs110\n")

order_total = 0
ordering = True

# Loop to take orders until the user decides to stop
while ordering:
    item = input("Enter the name of the item you want to order = ").title()
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order. Current total: Rs{order_total}")
    else:
        print(f"Ordered item {item} is not available yet!")
    
    # Ask if the user wants to add another item
    another_order = input("Do you want to add another item? (Yes/No) ").title()
    if another_order == "No":
        ordering = False  # Exit the loop

# Final order total
print(f"The total amount to pay is Rs{order_total}")
