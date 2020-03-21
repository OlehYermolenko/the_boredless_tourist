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
# print(get_destination_index('Los Angeles, USA'))

# Function to retrieve the index of the destination where the traveler is
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

# Test function
# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# Create and maintain a list of attractions
# Create an empty list for every destination in destinations
attractions = [[] for destination in destinations]

# Find the index of the destination
# Catch ValueError if destination doesn't exist
# Add attraction to attractions list
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        return

# Test function
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
# print(attractions)

# Add more places
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
