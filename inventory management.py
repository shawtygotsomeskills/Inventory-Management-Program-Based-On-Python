import csv
import matplotlib.pyplot as plt

# Inventory dictionary
inventory = {
    "Notebook": {"quantity": 20, "price": 50},
    "Pen": {"quantity": 50, "price": 10},
    "Bag": {"quantity": 10, "price": 800},
    "Pencil": {"quantity": 40, "price": 5}
}

# Sales dictionary
sales = {}


# Function to add item
def add_item():
    name = input("Enter item name: ")

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        if quantity <= 0 or price <= 0:
            print("Quantity and price must be greater than 0.")
            return

        if name in inventory:
            inventory[name]["quantity"] += quantity
            inventory[name]["price"] = price
        else:
            inventory[name] = {
                "quantity": quantity,
                "price": price
            }

        print("Item added successfully!")

    except ValueError:
        print("Please enter valid numbers.")


# Function to display inventory
def view_inventory():
    print("\n========== CURRENT INVENTORY ==========")

    print(f"{'Item':<15}{'Quantity':<10}{'Price':<10}")

    for name, details in inventory.items():
        print(f"{name:<15}{details['quantity']:<10}{details['price']:<10}")

    print("=======================================")


# Function to search item
def search_item():
    name = input("Enter item name to search: ")

    if name in inventory:
        print("\nItem Found!")
        print("Name:", name)
        print("Quantity:", inventory[name]["quantity"])
        print("Price:", inventory[name]["price"])
    else:
        print("Item not found.")


# Function to sell item
def sell_item():
    name = input("Enter item name: ")

    if name not in inventory:
        print("Item not found.")
        return

    try:
        quantity = int(input("Enter quantity sold: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > inventory[name]["quantity"]:
            print("Not enough stock available.")
            return

        # Reduce stock
        inventory[name]["quantity"] -= quantity

        # Calculate sale amount
        amount = quantity * inventory[name]["price"]

        # Add to sales
        if name in sales:
            sales[name] += amount
        else:
            sales[name] = amount

        print("Sale recorded successfully!")
        print("Total sale amount:", amount)

        # Low stock warning
        if inventory[name]["quantity"] <= 5:
            print("WARNING: Stock is running low!")

    except ValueError:
        print("Please enter a valid quantity.")


# Function to show sales summary
def sales_summary():
    print("\n========== SALES SUMMARY ==========")

    if len(sales) == 0:
        print("No sales have been recorded yet.")
        return

    total_sales = 0

    for item, amount in sales.items():
        print(f"{item:<15} Rs. {amount:.2f}")
        total_sales += amount

    print("-----------------------------------")
    print("TOTAL SALES: Rs.", total_sales)
    print("===================================")


# Function to export report
def export_report():
    with open("inventory_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # Inventory section
        writer.writerow(["INVENTORY REPORT"])
        writer.writerow(["Item", "Quantity", "Price", "Stock Value"])

        for name, details in inventory.items():
            stock_value = details["quantity"] * details["price"]

            writer.writerow([
                name,
                details["quantity"],
                details["price"],
                stock_value
            ])

        writer.writerow([])

        # Sales section
        writer.writerow(["SALES REPORT"])
        writer.writerow(["Item", "Total Sales"])

        for item, amount in sales.items():
            writer.writerow([item, amount])

        writer.writerow([])
        writer.writerow(["TOTAL SALES", sum(sales.values())])

    print("Report exported successfully!")
    print("File name: inventory_report.csv")


# Function to display graph
def show_graph():

    if len(sales) == 0:
        print("No sales data available for graph.")
        return

    items = list(sales.keys())
    amounts = list(sales.values())

    plt.bar(items, amounts)

    plt.title("Sales by Product")
    plt.xlabel("Products")
    plt.ylabel("Sales Amount (Rs.)")

    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.show()


# Main program
while True:

    print("\n")
    print("========================================")
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Search Item")
    print("4. Sell Item")
    print("5. View Sales Summary")
    print("6. Export Report to CSV")
    print("7. Show Sales Graph")
    print("8. Exit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        search_item()

    elif choice == "4":
        sell_item()

    elif choice == "5":
        sales_summary()

    elif choice == "6":
        export_report()

    elif choice == "7":
        show_graph()

    elif choice == "8":
        print("Thank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
