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
add_attraction('Paris, France', ['the Louvre', ['art', 'museum']])
add_attraction('Paris, France', ['Arc de Triomphe', ['historical site', 'monument']])
add_attraction('Shanghai, China', ['Yu Garden', ['garden', 'historcical site']])
add_attraction('Shanghai, China', ['Yuz Museum', ['art', 'museum']])
add_attraction('Shanghai, China', ['Oriental Pearl Tower', ['skyscraper', 'viewing deck']])
add_attraction('Los Angeles, USA', ['LACMA', ['art', 'museum']])
add_attraction('São Paulo, Brazil', ['São Paulo Zoo', ['zoo']])
add_attraction('São Paulo, Brazil', ['Pátio do Colégio', ['historical site']])
add_attraction('Cairo, Egypt', ['Pyramids of Giza', ['monument', 'historical site']])
add_attraction('Cairo, Egypt', ['Egyptian Museum', ['museum']])

# Function which matches traveler's interests with possible locations in the city
def find_attractions(destination, interests):
    # City's destination_index to look up its attractions in attractions table
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    # If the attraction match one of the interests attraction is will be saved to list
    attractions_with_interest = []

    # Retrieve tagged information for each attraction
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]

        # See if any of the given interests is in attraction_tags
        for interest in interests:
            if interest in attraction_tags:
                # Append only the nme of each attraction in order not to show tags
                attractions_with_interest.append(possible_attraction[0])

    return attractions_with_interest

# Test function
# la_arts = find_attractions('Los Angeles, USA', ['art'])
# print(la_arts)

# Connect people with attractions that they are interested in
def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    
    interests_string = 'Hi '+ traveler[0] + ', we think you\'ll like these places around ' + traveler_destination + ': '
    # If last attraction in list - add period, else add coma and space

    for i in range(len(traveler_attractions)):
        # Check if current attraction is the last one
        # If it is the last one - format interests_string differently
        if traveler_attractions[-1] == traveler_attractions[i]:
            interests_string += 'the ' + traveler_attractions[i] + '.'
        else:
            interests_string += 'the ' + traveler_attractions[i] + ', '

    return interests_string

# Test function
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)