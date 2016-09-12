#   codecademy
#   coding exercise
#   Python course

#   "Vacation"

def hotel_cost(nights):
    
    one_night = 140
    total_hotel = one_night * nights
    return total_hotel
    
#    *** Version A: if, elif, else clause ***

def plane_ride_cost(city):
    total_plane = "No valid flight destination"
    if city == "Charlotte":
        total_plane = 183
    elif city == "Tampa":
        total_plane = 220
    elif city == "Pittsburgh":
        total_plane = 222
    elif city == "Los Angeles":
        total_plane = 475
    else:
        print"Please enter a valid flight destination"
    return total_plane
 
#   *** Version B: for-loop
#   *** through Dictionary ***

    
def plane_ride_cost(city):
    city = str(city)
    
    plane_prices = {"Charlotte":183,"Tampa":220,"Pittsburgh":222,"Los Angeles":475}
    
    for key in plane_prices:
        if key == city:
            print plane_prices[city]
            return plane_prices[city]
            

def rental_car_cost(days):
    
    one_day = 40
    total_car = days * one_day
    
    if days >= 7:
        total_car -= 50
    elif days >= 3:
        total_car -=20
    return total_car
    
#   *** Now add it all up for the total trip cost ... ***
#   Note for calculation purposes:
#   nights = days

    
def trip_cost(city,days,spending_money):
    total_trip=rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)
    + spending_money
    
    return total_trip
    
print trip_cost("Los Angeles",5,600)
    
