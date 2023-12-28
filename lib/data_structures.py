spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food['name'] for food in spicy_foods]
result = get_names(spicy_foods)
print(result)   

def get_spiciest_foods(spicy_foods):
      return[food for food in spicy_foods if food["heat_level"] > 5]
result=get_spiciest_foods(spicy_foods)
print(result)

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level= food["heat_level"]

        heat_chilli = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_chilli}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
result = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result)
results= get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(results)

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    total_spice = sum(food["heat_level"] for food in spicy_foods)
    num_foods = len(spicy_foods)

    if num_foods == 0:
        return 0
    return total_spice // num_foods
result = get_average_heat_level(spicy_foods)
print(result)

def create_spicy_food(spicy_foods, spicy_food):
    pass
