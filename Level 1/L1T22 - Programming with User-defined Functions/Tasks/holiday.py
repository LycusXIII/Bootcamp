def hotel_cost(num_nights):
    '''
    Calculates the total cost of the hotel.
    Args:
        num_nights: The number of nights the user will be staying.
    Returns:
        The total cost of the hotel (price per night * number of nights)
    '''
    # Sets the cost per night
    cost_per_night = 1000
    return cost_per_night * num_nights

def plane_cost(city_flight):
    '''
        Calculates cost of the plane ticket based on the users input and chosen city.
    Args:
        city_flight: The city the user choose to for their flight.
    Returns:
        The cost of the plane ticket to the chosen city.
    '''
    # Sets the ticket price per city.
    ticket_price = 0
    if city_flight == "tokyo":
        ticket_price = 5000
    elif city_flight == "new york":
        ticket_price = 6000
    elif city_flight == "london":
        ticket_price = 3000
    elif city_flight == "johannesburg":
        ticket_price = 500
    
    return ticket_price

def car_rental(rental_days):
    '''
        Calculates the cost of the car rental based on the number of days the user is renting for.
    Args:
        rental_days: The amount of days the user is renting the car for.
    Returns:
        The total cost of car rental for user defined number of days.
    '''
    # Calculates rental price
    return rental_days * 50

def holiday_cost(hotel_cost, plane_cost, car_rental):
    '''
        Calculates the total cost of the holiday.
    Args:
        hotel_cost, plane_cost, car_rental: Values from other functions after
        calculations from user input.
    Returns:
        The total cost of the holiday.
    '''
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

cities = ["Tokyo", "New York", "London", "Johannesburg"]
lowered_cities = [city.lower() for city in cities] # makes another list of all lowercase.

while True:
    try:
        print(", ".join(cities)) # Displays the available cities
        city_flight = input("Pick one of the cities form the list above.\n").lower()
        if city_flight in lowered_cities:
            num_nights = int(input("How many nights will you be staying in a hotel? "))
            rental_days = int(input("How many days will you be renting a car? "))
            break
        else:
            print("Invalid input please select a city from the list below.")
            print(", ".join(cities))
    except ValueError:
        print("Invalid input please try again.")

# Calculates teh total cost of the holiday by calling the holiday 
# function and passing the required arguments.
total_cost = holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))

# Prints out the details in a nice readable format.
print(u'\u2500' * 50)
print("Holiday details:")
print(f"City:                   {city_flight.title()}")
print(f"Night:                  {num_nights}")
print(f"Car rental days:        {rental_days}")
print(f"Plane cost:             R{plane_cost(city_flight)}")
print(f"Hotel cost:             R{hotel_cost(num_nights)}")
print(f"Car rental cost:        R{car_rental(rental_days)}")
print(f"Total holiday cost:     R{total_cost}")
print(u'\u2500' * 50)