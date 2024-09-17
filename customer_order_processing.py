# 3 Customer Order Processing
# Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# - Write a function to iterate over the list of orders. 
# - Unpack each tuple in the list and format the details for display.

# Define the orders
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Carl", "Phone", 1),
    ("David", "Laptop", 2),
    ("Elena", "Monitor", 3),
    ("Frank", "Phone", 5)
]

def format_orders(orders):
    '''This function takes a list of orders as tuples (name, product, quantity) and displays them in a user-friendly format.'''
    try:
        # Iterate over each order
        for i, order in enumerate(orders):
            # Check the order is in the correct format
            if isinstance(order, tuple) and len(order)==3:
                # Print in a user-friendly format.
                print(f"Order #{i+1}: {order[0]} ordered {order[2]} {order[1].lower()}(s).")
            else: 
                raise ValueError
    except ValueError:
        print("Invalid input. Try again!")

format_orders(orders)