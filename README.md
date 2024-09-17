# Module 3 - Lesson 2 - Python Tuples
Author: Elizabeth Yates

1. Tuple Mastery in Python 

Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

Task 1: Formatting Flight Itineraries (formatting_flight_itineraries.py)

Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. 

For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"

 2. Python Data Structure Challenges in Real-World Scenarios

Task 1: Library System Enhancement (library_system_enhancement.py)

Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

3. Mastering Tuple Packing and Unpacking in Python

Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

Task 1: Customer Order Processing (customer_order_processing.py)

Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
- Write a function to iterate over the list of orders. 
- Unpack each tuple in the list and format the details for display.