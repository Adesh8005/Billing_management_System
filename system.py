class BillingSystem:
    def __init__(self):          
        self.items = []  # To store items as a list of dictionaries
        self.total = 0

    def add_item(self, name, quantity, price):
        """
        Add an item to the bill.
        :param name: Name of the item
        :param quantity: Quantity of the item
        :param price: Price per unit of the item
        """
        item = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        }
        self.items.append(item)
        self.total += item["total"]
        print(f"Added {quantity}x {name} @ {price} each. Subtotal: {item['total']}")

    def display_bill(self):
        """
        Display the bill with all items and total cost.
        """
        print("\n" + "=" * 30)
        print("          BILL SUMMARY         ")
        print("=" * 30)
        print(f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total':<10}")
        print("-" * 30)
        for item in self.items:
            print(f"{item['name']:<15}{item['quantity']:<5}{item['price']:<10}{item['total']:<10}")
        print("-" * 30)
        print(f"{'TOTAL':<15}{'':<5}{'':<10}{self.total:<10}")
        print("=" * 30)

    def reset(self):
        """
        Reset the bill by clearing all items and total.
        """
        self.items = []
        self.total = 0
        print("Bill has been reset!")


def main():
    system = BillingSystem()

    while True:
        print("\n" + "=" * 30)
        print("       Billing Management     ")
        print("=" * 30)
        print("1. Add Item to Bill")
        print("2. Show Bill")
        print("3. Reset Bill")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            system.add_item(name, quantity, price)
        elif choice == "2":
            system.display_bill()
        elif choice == "3":
            system.reset()
        elif choice == "4":
            print("Thank you for using the Billing System!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
