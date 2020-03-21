# Create list with destinations
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

# Define a test traveler to see how functionality is working so far
# This is a traveler (a user of the application)
# Whose name is Erin Wilkes who likes historical buildings and art. Erin is in China right now
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# When a traveler arrives at a destination, we want to know where they are
# Identify each location based on its index in destinations list
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

# Test function
print(get_destination_index('Los Angeles, USA'))

# Function to retrieve the index of the destination where the traveler is
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Test function
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)