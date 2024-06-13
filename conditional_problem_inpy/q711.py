import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
import random

class CoffeeShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop App")

        # Setup style
        style = ttk.Style()
        style.theme_use('clam')

        # Order Summary Treeview
        self.tree = ttk.Treeview(root, columns=("Item", "Quantity", "Extra Shot", "Price"), show='headings')
        self.tree.heading("Item", text="Item")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Extra Shot", text="Extra Shot")
        self.tree.heading("Price", text="Price")
        self.tree.column("Item", anchor=tk.CENTER)
        self.tree.column("Quantity", anchor=tk.CENTER)
        self.tree.column("Extra Shot", anchor=tk.CENTER)
        self.tree.column("Price", anchor=tk.CENTER)
        self.tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Coffee Variety Dropdown
        ttk.Label(root, text="Coffee:").grid(row=1, column=0, padx=10, pady=5)
        self.coffee_var = tk.StringVar()
        self.coffee_var.set("Espresso")  # Default value
        self.coffee_options = ["Espresso", "Americano", "Latte", "Cappuccino"]
        self.coffee_menu = ttk.OptionMenu(root, self.coffee_var, *self.coffee_options)
        self.coffee_menu.grid(row=1, column=1, padx=10, pady=5)

        # Quantity Entry
        ttk.Label(root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
        self.quantity_var = tk.IntVar()
        self.quantity_entry = ttk.Entry(root, textvariable=self.quantity_var)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        # Extra Shot Checkbox
        self.extra_shot_var = tk.BooleanVar()
        self.extra_shot_check = ttk.Checkbutton(root, text="Extra Shot (+$1)", variable=self.extra_shot_var)
        self.extra_shot_check.grid(row=2, column=2, padx=10, pady=5)

        # Add to Order Button
        self.add_button = ttk.Button(root, text="Add to Order", command=self.add_to_order)
        self.add_button.grid(row=3, column=0, padx=10, pady=5)

        # Save and Load Buttons
        self.save_button = ttk.Button(root, text="Save Orders", command=self.save_orders)
        self.save_button.grid(row=3, column=1, padx=10, pady=5)

        self.load_button = ttk.Button(root, text="Load Orders", command=self.load_orders)
        self.load_button.grid(row=3, column=2, padx=10, pady=5)

        # Discount Code Entry
        ttk.Label(root, text="Discount Code:").grid(row=4, column=0, padx=10, pady=5)
        self.discount_var = tk.StringVar()
        self.discount_entry = ttk.Entry(root, textvariable=self.discount_var)
        self.discount_entry.grid(row=4, column=1, padx=10, pady=5)

        # Apply Discount Button
        self.apply_discount_button = ttk.Button(root, text="discount", command=self.apply_discount)
        self.apply_discount_button.grid(row=4, column=2, padx=10, pady=5)

        # Reset Button
        self.reset_button = ttk.Button(root, text="Reset", command=self.reset_order)
        self.reset_button.grid(row=5, column=0, padx=10, pady=5)

        # Print Button
        self.print_button = ttk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=5, column=1, padx=10, pady=5)

        # Receipt Display
        ttk.Label(root, text="Receipt:").grid(row=6, column=0, padx=10, pady=5)
        self.receipt_text = tk.Text(root, height=15, width=50)
        self.receipt_text.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

        self.orders = []
        self.order_id = self.generate_order_id()

    def generate_order_id(self):
        return random.randint(1000, 9999)

    def add_to_order(self):
        # debbuger this code 
        item = self.coffee_var.get()
        quantity = self.quantity_var.get()
        extra_shot = self.extra_shot_var.get()
        price_per_item = 5.0 + (1.0 if extra_shot else 0)  # Extra $1 for extra shot
        total_price = price_per_item * quantity

        if quantity > 0:
            self.tree.insert("", "end", values=(item, quantity, "Yes" if extra_shot else "No", f"${total_price:.2f}"))
            self.orders.append((item, quantity, extra_shot, total_price))
            self.update_receipt()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid quantity.")

    def save_orders(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Item", "Quantity", "Extra Shot", "Price"])
                for order in self.orders:
                    item, quantity, extra_shot, price = order
                    writer.writerow([item, quantity, "Yes" if extra_shot else "No", f"${price:.2f}"])
            messagebox.showinfo("Save Success", "Orders saved successfully!")

    def load_orders(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.orders = []
                for row in reader:
                    item, quantity, extra_shot, price = row
                    quantity = int(quantity)
                    extra_shot = (extra_shot == "Yes")
                    price = float(price.replace('$', ''))
                    self.tree.insert("", "end", values=(item, quantity, "Yes" if extra_shot else "No", f"${price:.2f}"))
                    self.orders.append((item, quantity, extra_shot, price))
            self.update_receipt()
            messagebox.showinfo("Load Success", "Orders loaded successfully!")

    def apply_discount(self):
        # Fix: make this discount in radio button , so that you won't have to write the discount code every time
        discount_code = self.discount_var.get()
        discount_amount = 5.0  # Example discount logic
        self.receipt_text.insert(tk.END, f"Discount Applied: {discount_code} - ${discount_amount:.2f}\n")
        self.update_receipt(discount_amount)

    def update_receipt(self, discount=0):
        self.receipt_text.delete(1.0, tk.END)
        total = 0
        self.receipt_text.insert(tk.END, f"Order ID: {self.order_id}\n")
        self.receipt_text.insert(tk.END, "Receipt:\n")
        for order in self.orders:
            item, quantity, extra_shot, price = order
            self.receipt_text.insert(tk.END, f"{item} x{quantity} {'(Extra Shot)' if extra_shot else ''} - ${price:.2f}\n")
            total += price
        if discount:
            total -= discount
            self.receipt_text.insert(tk.END, f"Discount: -${discount:.2f}\n")
        self.receipt_text.insert(tk.END, f"Total: ${total:.2f}\n")

    def reset_order(self):
        self.orders = []
        self.tree.delete(*self.tree.get_children())
        self.receipt_text.delete(1.0, tk.END)
        self.discount_var.set("")
        self.order_id = self.generate_order_id()

    def print_receipt(self):
        receipt_content = self.receipt_text.get(1.0, tk.END)
        print(receipt_content)  # For now, just print to the console. You could integrate with an actual printer if needed.
        messagebox.showinfo("Print Success", "Receipt printed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeShopApp(root)
    root.mainloop()
