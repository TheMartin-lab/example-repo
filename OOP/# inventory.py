# inventory.py
#Joshua Martin
#JO25080018810
# Shoe class definition
# =========================
# Shoe Class
# =========================
class Shoe:
    """Represents a single shoe with its details."""

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a new Shoe object.
        
        Args:
            country (str): Country of origin
            code (str): Unique shoe code
            product (str): Product name
            cost (float): Price per shoe
            quantity (int): Quantity in stock
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe in stock."""
        return self.quantity

    def __str__(self):
        """Return a formatted string representing the shoe."""
        return (
            f"{self.country}, {self.code}, {self.product}, "
            f"Cost: {self.cost}, Quantity: {self.quantity}"
        )


# =========================
# Global List
# =========================
shoe_list = []  # List to store Shoe objects


# =========================
# Functions
# =========================
def read_shoes_data():
    """
    Read shoe data from 'inventory.txt' and populate shoe_list.
    Skips the header line. Prints error if file is not found.
    """
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("File not found.")


def capture_shoes():
    """
    Prompt user to enter shoe details and add new Shoe to shoe_list.
    """
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")

    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print("Shoe captured successfully.")


def view_all():
    """
    Display all shoes in the shoe_list.
    """
    if not shoe_list:
        print("No shoes available.")
        return
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    """
    Find the shoe with the lowest quantity and allow user to add stock.
    """
    if not shoe_list:
        print("No shoes available to restock.")
        return

    # Find shoe with lowest quantity
    lowest = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < lowest.quantity:
            lowest = shoe

    print("Lowest stock item:")
    print(lowest)

    try:
        add_qty = int(input("Enter quantity to add: "))
        lowest.quantity += add_qty
        print(f"Updated quantity: {lowest.quantity}")
    except ValueError:
        print("Invalid input. Quantity must be an integer.")


def search_shoe():
    """
    Search for a shoe by its code and display it.
    
    Returns:
        Shoe object if found, None otherwise.
    """
    search_code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("Shoe found:")
            print(shoe)
            return shoe
    print("Shoe not found.")
    return None


def value_per_item():
    """
    Calculate and print the total value of each shoe in stock
    (cost multiplied by quantity).
    """
    if not shoe_list:
        print("No shoes available.")
        return
    print("Total value per item:")
    for shoe in shoe_list:
        total_value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {total_value}")


def highest_qty():
    """
    Determine and display the shoe with the highest quantity in stock.
    """
    if not shoe_list:
        print("No shoes available.")
        return

    highest = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity > highest.quantity:
            highest = shoe

    print("Shoe with highest quantity (for sale):")
    print(highest)


# =========================
# Main Menu
# =========================
def main_menu():
    """
    Display a menu to the user to perform various operations on shoe inventory.
    Calls the appropriate function based on user input.
    """
    read_shoes_data()  # Load inventory at program start

    while True:
        print("\n===== Shoe Inventory Menu =====")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Restock shoe")
        print("4. Search shoe by code")
        print("5. Show value per item")
        print("6. Show shoe with highest quantity")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock()
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


# =========================
# Program Start
# =========================
if __name__ == "__main__":
    main_menu()
