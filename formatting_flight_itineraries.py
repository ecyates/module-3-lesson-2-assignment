# 1 - Formatting Flight Itineraries
# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). 
# 
# The function should format and return a string that lists each itinerary. 
#
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:
#
# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

def format_flight_itineraries(flight_itineraries):
    '''This function formats the flight itineraries and returns a string that lists each itinerary.'''
    try: 
        # If the list is empty, raise error
        if flight_itineraries == []: 
            raise ValueError()
        else:
            # Create the string we'll be returning
            formatted_itineraries = ""
            # Iterate through the list of tuples
            for i, passenger in enumerate(flight_itineraries):
                if isinstance(passenger, tuple):
                    # Add the new line for each itinerary
                    formatted_itineraries += f"\nItinerary {i+1}: {passenger[0]} - From {passenger[1]} to {passenger[2]}"
                # If one of the entries isn't a tuple, raise error
                else: 
                    raise ValueError()
    except ValueError:
        print("Invalid input. Correct input: [(name, origin, destination)]")
    except IndexError:
        print("Invalid input. Correct input: [(name, origin, destination)]")
    else:
        return formatted_itineraries
        

# Checking a normal entry
flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Craig", "Portland", "Atlanta"), ("Daniela", "Mexico City", "Houston"), ("Elizabeth", "Sacramento", "Los Angeles")]
formatted_itineraries = format_flight_itineraries(flight_itineraries)
print(formatted_itineraries)

# Checking if the list is empty
testing = []
format_flight_itineraries(testing)

# Checking what happens if the elements are invalid
testing = ["Alice", "Bob", "Carla"]
format_flight_itineraries(testing)

# Checking what happens if the tuples are the wrong size
testing = [("Alice", "New York"), ("London"), ("Bob", "Tokyo", "San Francisco")]
format_flight_itineraries(testing)