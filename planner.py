import math

# KNOWLEDGE BASE

city_info = {
    "Hyderabad": {
        "places": {
            "history": [
                "Charminar",
                "Golconda Fort",
                "Salar Jung Museum"
            ],
            "nature": [
                "Hussain Sagar",
                "NTR Garden"
            ],
            "food": [
                "Biryani Spots",
                "Irani Cafe"
            ]
        },

        "hotel_cost": {
            "low": 1000,
            "medium": 2500,
            "high": 5000
        },

        "transport_per_day": 500,

        "food_options": {
            "veg": [
                "Veg Biryani",
                "Paneer Curry"
            ],
            "non-veg": [
                "Chicken Biryani",
                "Mutton Biryani"
            ]
        }
    }
}

# TRAVEL PLANNER FUNCTION

def create_travel_plan(destination,
                       amount,
                       total_days,
                       category,
                       food_type):

    if destination not in city_info:
        print("City not available")
        return

    details = city_info[destination]

    if amount < 5000:
        stay_type = "low"
    elif amount < 15000:
        stay_type = "medium"
    else:
        stay_type = "high"

    stay_cost = details["hotel_cost"][stay_type] * total_days
    travel_cost = details["transport_per_day"] * total_days
    meal_cost = 400 * total_days

    final_cost = stay_cost + travel_cost + meal_cost

    visit_list = details["places"].get(category, [])
    food_list = details["food_options"].get(food_type, [])

    print("\nAI TRAVEL PLAN")
    print("-----------------------------")

    print("Destination :", destination)
    print("Budget      : ₹", amount)
    print("Days        :", total_days)

    print("\nRecommended Places:")

    for place_name in visit_list:
        print("-", place_name)

    print("\nRecommended Food:")

    for food_item in food_list:
        print("-", food_item)

    print("\nHotel Type :", stay_type)

    print("\nEstimated Cost")
    print("Hotel Cost     : ₹", stay_cost)
    print("Transport Cost : ₹", travel_cost)
    print("Food Cost      : ₹", meal_cost)

    print("-----------------------------")
    print("Total Cost     : ₹", final_cost)

    print("\nDAY WISE PLAN")

    places_each_day = math.ceil(len(visit_list) / total_days)

    position = 0

    for day_no in range(1, total_days + 1):

        print("\nDay", day_no)

        for _ in range(places_each_day):

            if position < len(visit_list):
                print("- Visit", visit_list[position])
                position += 1

        if food_list:
            print("- Try:", food_list[0])


# MAIN PROGRAM

print("SMART AI TRAVEL PLANNER")

destination = input("Enter city (Hyderabad): ")

amount = int(input("Enter budget: ₹"))

total_days = int(input("Enter number of days: "))

category = input(
    "Enter interest "
    "(history/nature/food): "
).lower()

food_type = input(
    "Food preference "
    "(veg/non-veg): "
).lower()

create_travel_plan(
    destination,
    amount,
    total_days,
    category,
    food_type
)
